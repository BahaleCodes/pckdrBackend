from rest_framework import serializers
from .models import Patient, Doctor, Address, MedRecords, Diagnostics, Sickness, DiagnosticsDesc, SergicalRecord, ObstericsRecord, Prescription, PregnancyComplications, Allergies, Exam, Treatment

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = 'id', 'FName', 'LName', 'Email', 'IdNum', 'user', 'gender', 'race'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = 'doctorId', 'FName', 'LName', 'Email', 'IdNum', 'user', 'regNum', 'officePhone', 'speciality'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = 'addressId', 'country', 'province', 'city', 'zipCode', 'addressLine1'

class MedRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedRecords
        fields = 'id', 'diagnosticsId', 'sergicalRecordId', 'obstrericId', 'allergiesId', 'examsId'

class DiagnosticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnostics
        fields = 'diagnosticsId', 'treatmentId', 'sicknessId', 'diagnosticsDescId', 'doctorId'

class SicknessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sickness
        fields = 'sicknessId', 'illness', 'symptoms', 'chronic'

class DiagnosticsDescSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnosticsDesc
        fields = 'diagnosticsDescId', 'cause', 'symptomsDesc'

class SergicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = SergicalRecord
        fields = 'sergicalRecordId', 'sergType', 'progressReport', 'operationDate', 'doctorId', 'diagnosticsId'

class PregnancyComplicationsSerializers(serializers.ModelSerializer):
    class Meta:
        model = PregnancyComplications
        fields = 'complicationId', 'complication', 'description'

class ObstericsRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObstericsRecord
        fields = 'obstericRecordId', 'pregnancies', 'date', 'complicationId', 'doctorId', 'diagnosticsId'

class AllergiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergies
        fields = 'allergiesId', 'symptoms', 'diagnosticsId'
        
class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = 'examId', 'examType', 'date', 'doctorId', 'diagnosticsId'

class TreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treatment
        fields = 'treatmentId', 'method', 'prescriptionId'
        
class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = 'prescriptionId', 'prescribedMeds', 'usage', 'prescribedAmount', 'start', 'finish'