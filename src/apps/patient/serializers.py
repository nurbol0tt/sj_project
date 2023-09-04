from rest_framework import serializers
from .models.patient_models import Patient, PatientInfo
from django.db.models import Model

from .models.info_models import (
    AnamnesisDisease, AnamnesisLife, SomaticStatus, NeurologicalStatus, MentalStatus,
    Category, TypeIntoxication, TypeTolerance, TypePalimpsests, Category, TypeTolerance
)


class AnamnesisLifeSerializers(serializers.ModelSerializer):

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
        AnamnesisLife.objects.create(patient=patient, **anamnesis_life_data)  # Create the related instance
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
            return "http://127.0.0.1:8000/" + obj.avatar.url


class AnamnesisDiseaseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AnamnesisDisease
        fields = '__all__'


class SomaticStatusSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SomaticStatus
        fields = '__all__'


class NeurologicalStatusSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = NeurologicalStatus
        fields = '__all__'


class MentalStatusSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MentalStatus
        fields = '__all__'


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
            'departament', 'number_of_days', 'blood_type', 'patient',
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
            anamnesis_instance.category.add(category_data)

        for type_tolerance in type_tolerances:
            anamnesis_instance.type_tolerance.add(type_tolerance)

        for type_intoxication in type_intoxications:
            anamnesis_instance.type_intoxication.add(type_intoxication)

        for type_palimpsest in type_palimpsests:
            anamnesis_instance.type_palimpsests.add(type_palimpsest)

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