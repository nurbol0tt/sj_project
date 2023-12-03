from rest_framework import serializers

from .models.comment_models import Diary, Photo, PsychologicalConsultation
from .models.emcrisis_models import Epicrisis
from .models.patient_models import Patient, PatientInfo
from django.db.models import Model

from .models.info_models import (
    AnamnesisDisease,
    AnamnesisLife,
    SomaticStatus,
    NeurologicalStatus,
    MentalStatus
)
from ...config import settings


class AnamnesisLifeSerializers(serializers.ModelSerializer):
    education = serializers.CharField(source='get_education_display', read_only=True)
    martial_status = serializers.CharField(source='get_martial_status_display', read_only=True)

    class Meta:
        model = AnamnesisLife
        fields = (
            'education', 'martial_status', 'place_work',
            'criminal_record', 'previous_illnesses', 'medications',
            'allergic_history',
        )


class PatientCreateSerializer(serializers.ModelSerializer):
    anamnesis_life = AnamnesisLifeSerializers()
    
    class Meta:
        model = Patient
        fields = (
            'name', 'surname', 'patronymic',
            'date_of_birth', 'anamnesis_life'
        )

    def create(self, validated_data):
        anamnesis_life_data = validated_data.pop('anamnesis_life')  # Extract the nested data
        patient = Patient.objects.create(**validated_data)
        AnamnesisLife.objects.create(patient=patient, **anamnesis_life_data)
        return patient

    def update(self, instance: Model, validated_data):
        anamnesis_life_data = validated_data.pop('anamnesis_life', {})
        anamnesis_life_instance = instance.anamnesis_life

        # Update main instance fields
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        # Update AnamnesisLife fields
        for key, value in anamnesis_life_data.items():
            setattr(anamnesis_life_instance, key, value)
        anamnesis_life_instance.save()

        return instance


class PatientListSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = Patient
        fields = ('id', 'name', 'surname', 'patronymic', 'avatar', 'in_hospital')

    def get_avatar(self, obj):
        if obj.avatar:
            return "http://139.59.132.105" + obj.avatar.url


class PatientInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientInfo
        fields = ('id', 'date_of_admission', 'date_of_discharge',)


class PatientDetailSerializer(serializers.ModelSerializer):
    anamnesis = AnamnesisLifeSerializers(source='anamnesis_life')
    patient_info = PatientInfoSerializer(
        many=True, read_only=True
    )
    patient_info_count = serializers.SerializerMethodField()
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = Patient
        fields = (
            'id', 'name', 'surname', 'patronymic',
            'avatar', 'in_hospital', 'date_of_birth', 'anamnesis',
            'patient_info_count', 'patient_info',
        )

    def get_avatar(self, obj):
        if obj.avatar:
            return settings.PHOTO_URL + obj.avatar.url

    def get_patient_info_count(self, obj):
        return obj.patient_info.count()


class SomaticStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = SomaticStatus
        fields = (
            'id', 'condition', 'category', 'skin_type', 'availability',
            'traces', 'state_conjunctiva', 'breath', 'wheezing', 'bh',
            'saturation', 'heart_tones', 'ad', 'pulse_frequency',
            'filling', 'tongue', 'stomach', 'liver', 'vomiting', 'stool',
            'diuresis', 'edema', 'glucose', 'apparatus', 'vascular_system',
            'supplements',
        )


class NeurologicalStatusSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = NeurologicalStatus
        fields = (
            'id', 'pupils', 'photo_reaction',
            'meningeal_signs', 'seizures', 'dysarthria'
        )


class MentalStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = MentalStatus
        fields = (
            'id', 'view', 'smell_of_alcohol', 'behavior',
            'consciousness', 'orientation', 'perception_disorders',
            'emotional_background', 'night_sleep', 'suicide_attempt',
            'causes_of_alcohol', 'purpose_of_hospitalization'
        )


class AnamnesisDiseaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnamnesisDisease
        fields = (
            'id', 'receiving_something', 'receiving_something_time', 'somatic_disorders',
            'mental_disorders', 'category', 'type_tolerance', 'type_intoxication',
            'type_palimpsests', 'daily_tolerance', 'binge_drinking', 'light_gaps',
            'duration_last_binge', 'duration_last_remission', 'last_treatment',
            'last_alcohol_intake', 'dose', 'addition'
        )


class PatientRecordSerializer(serializers.ModelSerializer):
    anamnesis = AnamnesisDiseaseSerializer()
    somatic = SomaticStatusSerializer()
    neurological = NeurologicalStatusSerializer()
    mental = MentalStatusSerializer()

    class Meta:
        model = PatientInfo
        fields = (
            'arrives', 'price', 'conditions', 'escorts', 'escorts',
            'complaints', 'date_of_admission', 'date_of_discharge',
            'departament', 'number_of_days', 'blood_type',
            'anamnesis', 'somatic', 'neurological', 'mental'
        )

    def create(self, validated_data):
        anamnesis_data = validated_data.pop('anamnesis')
        somatic_data = validated_data.pop('somatic')
        neurological_data = validated_data.pop('neurological')
        mental_data = validated_data.pop('mental')

        anamnesis_instance = AnamnesisDisease.objects.create(**anamnesis_data)
        somatic_instance = SomaticStatus.objects.create(**somatic_data)
        neurological_instance = NeurologicalStatus.objects.create(**neurological_data)
        mental_instance = MentalStatus.objects.create(**mental_data)

        # Create the PatientInfo instance with the remaining data
        patient_info = PatientInfo.objects.create(
            anamnesis=anamnesis_instance,
            somatic=somatic_instance,
            neurological=neurological_instance,
            mental=mental_instance,
            **validated_data
        )

        patient_info.save()
        return patient_info


class PatientPatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatientInfo
        fields = (
            'arrives', 'conditions', 'price',
            'escorts', 'complaints', 'date_of_admission',
            'date_of_discharge', 'departament', 'number_of_days', 'blood_type'
        )


class ContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Diary
        fields = (
            'id', 'content',
        )


class PsychologicalContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = PsychologicalConsultation
        fields = (
            'id', 'content'
        )


class PhotoSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Photo
        fields = (
            'file', 'user'
        )


class PhotoListSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()

    class Meta:
        model = Photo
        fields = (
            'id', 'file',
        )

    def get_file(self, obj):
        if obj.file:
            return settings.PHOTO_URL + obj.file.url


class EpicrisisSerializer(serializers.ModelSerializer):

    class Meta:
        model = Epicrisis
        fields = (
            'start_treatment', 'end_treatment', 'main_diagnosis',
            'concomitant', 'complications', 'laboratory_tests',
            'instrumental_studies', 'ecg', 'x_ray', 'specialist_consultations',
            'treatment', 'treatment_results', 'recommendations'
        )


class EpicrisisDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Epicrisis
        fields = (
            'id', 'start_treatment', 'end_treatment', 'main_diagnosis',
            'concomitant', 'complications', 'laboratory_tests',
            'instrumental_studies', 'ecg', 'x_ray', 'specialist_consultations',
            'treatment', 'treatment_results', 'recommendations'
        )

class EpicrisisSerializerList(serializers.ModelSerializer): # noqa

    class Meta:
        model = Epicrisis
        fields = (
            'id', 'start_treatment', 'end_treatment', 'concomitant',
        )


class PatientInfoIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientInfo
        fields = ('id', 'price', 'date_of_admission', 'date_of_discharge')


class PatientSerializer(serializers.ModelSerializer):
    patient_info = PatientInfoIncomeSerializer(many=True, read_only=True, source='patient_info.all')

    class Meta:
        model = Patient
        fields = (
            'id', 'name', 'surname',
            'patronymic', 'date_of_birth',
            'in_hospital', 'updated_at', 'patient_info'
        )

    def get_patient_profit(self, patient):
        return sum(info.price for info in patient.patient_info.all())

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['total_profit'] = self.get_patient_profit(instance)
        return data
