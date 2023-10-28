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
    MentalStatus,
    TypeIntoxication,
    TypePalimpsests,
    Category,
    TypeTolerance
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
        anamnesis_life_data = validated_data.pop('anamnesis_life')
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
        many=True, read_only=True, source='patientinfo_set',
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
        return obj.patientinfo_set.count()


class SomaticStatusSerializer(serializers.ModelSerializer):
    condition = serializers.CharField(source='get_condition_display', read_only=True)
    category = serializers.CharField(source='get_category_display', read_only=True)
    skin_type = serializers.CharField(source='get_skin_type_display', read_only=True)
    availability = serializers.CharField(source='get_availability_display', read_only=True)
    traces = serializers.CharField(source='get_traces_display', read_only=True)
    state_conjunctiva = serializers.CharField(source='get_state_conjunctiva_display', read_only=True)
    breath = serializers.CharField(source='get_breath_display', read_only=True)
    wheezing = serializers.CharField(source='get_wheezing_display', read_only=True)
    heart_tones = serializers.CharField(source='get_heart_tones_display', read_only=True)
    filling = serializers.CharField(source='get_filling_display', read_only=True)

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
    pupils = serializers.CharField(source='get_pupils_display', read_only=True)
    meningeal_signs = serializers.CharField(source='get_meningeal_signs_display', read_only=True)

    class Meta:
        model = NeurologicalStatus
        fields = (
            'id', 'pupils', 'photo_reaction',
            'meningeal_signs', 'seizures', 'dysarthria'
        )


class MentalStatusSerializer(serializers.ModelSerializer):
    view = serializers.CharField(source='get_view_display', read_only=True)

    class Meta:
        model = MentalStatus
        fields = (
            'id', 'view', 'smell_of_alcohol', 'behavior',
            'consciousness', 'orientation', 'perception_disorders',
            'emotional_background', 'night_sleep', 'suicide_attempt',
            'causes_of_alcohol', 'purpose_of_hospitalization'
        )


class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'title')


class TypeIntoxicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeIntoxication
        fields = ('id', 'title')


class TypeToleranceSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeTolerance
        fields = ('id', 'title')


class TypePalimpsestsSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypePalimpsests
        fields = ('id', 'title')


class AnamnesisDiseaseSerializer(serializers.ModelSerializer):
    category = CategoryListSerializer(many=True)
    type_tolerance = TypeToleranceSerializer(many=True)
    type_intoxication = TypeIntoxicationSerializer(many=True)
    type_palimpsests = TypePalimpsestsSerializer(many=True)

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
    # arrives = serializers.CharField(source='get_arrives_display')

    class Meta:
        model = PatientInfo
        fields = (
            'arrives', 'price', 'conditions', 'escorts', 'escorts',
            'complaints', 'date_of_admission', 'date_of_discharge',
            'departament', 'number_of_days', 'blood_type',
            'anamnesis', 'somatic', 'neurological', 'mental'
        )

    def create(self, validated_data):
        anamnesis_data = validated_data.pop('anamnesis', [])
        somatic_data = validated_data.pop('somatic')
        neurological_data = validated_data.pop('neurological')
        mental_data = validated_data.pop('mental')

        categories = anamnesis_data.pop('category')
        type_tolerances = anamnesis_data.pop('type_tolerance')
        type_intoxications = anamnesis_data.pop('type_intoxication')
        type_palimpsests = anamnesis_data.pop('type_palimpsests')

        anamnesis_instance = AnamnesisDisease.objects.create(**anamnesis_data)

        for category_data in categories:
            category = Category.objects.get(title=category_data['title'])
            anamnesis_instance.category.add(category)

        for tolerance_data in type_tolerances:
            tolerance = TypeTolerance.objects.get(title=tolerance_data['title'])
            anamnesis_instance.type_tolerance.add(tolerance)

        for intoxication_data in type_intoxications:
            intoxication = TypeIntoxication.objects.get(title=intoxication_data['title'])
            anamnesis_instance.type_intoxication.add(intoxication)

        for palimpsest_data in type_palimpsests:
            palimpsest = TypePalimpsests.objects.get(title=palimpsest_data['title'])
            anamnesis_instance.type_palimpsests.add(palimpsest)

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

    class Meta:
        model = Photo
        fields = (
            'file',
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
    treatment_results = serializers.CharField(source='get_treatment_results_display', read_only=True)

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
