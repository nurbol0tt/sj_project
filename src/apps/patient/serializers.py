from rest_framework import serializers
from .models.info_models import AnamnesisLife
from .models.patient_models import Patient


class AnamnesisLifeSerializers(serializers.ModelSerializer):

    class Meta:
        model = AnamnesisLife
        fields = (
            'education', 'martial_status', 'place_work',
            'criminal_record', 'previous_illnesses', 'medications', 'allergic_history'
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
    