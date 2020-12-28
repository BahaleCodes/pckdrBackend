from django.shortcuts import render
from rest_framework import viewsets
from .models import Patient, Doctor, Address, Exam, DiagnosticsDesc, Treatment, Sickness, MedRecords, Diagnostics, Allergies, ObstericsRecord, SergicalRecord, Prescription, PregnancyComplications
from .serializers import PatientSerializer, AddressSerializer, PrescriptionSerializer,TreatmentSerializer, AllergiesSerializer, PregnancyComplicationsSerializers, DoctorSerializer, DiagnosticsDescSerializer, DiagnosticsSerializer, PregnancyComplicationsSerializers, MedRecordsSerializer, SergicalRecordSerializer, ExamSerializer, ObstericsRecordSerializer, SicknessSerializer, SergicalRecordSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = (PatientSerializer)

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = (DoctorSerializer)

class AddressViewset(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = (AddressSerializer)

class MedRecordsViewSet(viewsets.ModelViewSet):
    queryset = MedRecords.objects.all()
    serializer_class = (MedRecordsSerializer)
    
class DiagnosticsViewset(viewsets.ModelViewSet):
    queryset = Diagnostics.objects.all()
    serializer_class = (DiagnosticsSerializer)
    
class SicknesViewset(viewsets.ModelViewSet):
    queryset = Sickness.objects.all()
    serializer_class = (SicknessSerializer)
    
class DiagnosticsDescViewset(viewsets.ModelViewSet):
    queryset = DiagnosticsDesc.objects.all()
    serializer_class = (DiagnosticsDescSerializer)

class SergicalRecordViewset(viewsets.ModelViewSet):
    queryset = SergicalRecord.objects.all()
    serializer_class = (SergicalRecordSerializer)
    
class PregnancyComplicationsViewset(viewsets.ModelViewSet):
    queryset = PregnancyComplications.objects.all()
    serializer_class = (PregnancyComplicationsSerializers)
    
class ObstericsRecordViewset(viewsets.ModelViewSet):
    queryset = ObstericsRecord.objects.all()
    serializer_class = (ObstericsRecordSerializer)
    
class AllergiesViewset(viewsets.ModelViewSet):
    queryset = Allergies.objects.all()
    serializer_class = (AllergiesSerializer)
    
class ExamViewset(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = (ExamSerializer)
    
class TreatmentViewset(viewsets.ModelViewSet):
    queryset = Treatment.objects.all()
    serializer_class = (TreatmentSerializer)
        
class PrescriptionViewset(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = (PrescriptionSerializer)