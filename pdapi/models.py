from django.db import models
from django.contrib.auth.models import User

class CommonInfo(models.Model):
    FName = models.CharField(max_length=50)
    LName = models.CharField(max_length=50)
    Email = models.EmailField()
    IdNum = models.IntegerField()
    class Mata:
        abstract = True

class Patient(CommonInfo):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    race = models.CharField(max_length=10)

class Doctor(CommonInfo):
    doctorId = models.CharField(max_length=8, primary_key=True, blank=True)
    SPECIALITIES = (
        ('GP', 'General practitioner'),
        ('OB/GYN', 'Obstetrician and Gynaecologist'),
        ('PSY', 'Psychiatrist'),
        ('DN', 'Dentist'),
        ('GS', 'General surgeon'),
        ('DM', 'Dermatologist'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    regNum = models.CharField(max_length=15)
    officePhone = models.IntegerField()
    speciality = models.CharField(max_length=6, choices=SPECIALITIES)

class Prescription(models.Model):
    prescriptionId = models.CharField(max_length=8, primary_key=True)
    prescribedMeds = models.CharField(max_length=100)
    usage = models.CharField(max_length=50)
    prescribedAmount = models.CharField(max_length=10)
    start = models.DateTimeField()
    finish = models.DateTimeField()

class Treatment(models.Model):
    treatmentId = models.CharField(max_length=8, primary_key=True)
    method = models.CharField(max_length=100)
    prescriptionId = models.ForeignKey(Prescription, on_delete=models.CASCADE)

class Sickness(models.Model):
    sicknessId = models.CharField(max_length=8, primary_key=True)
    illness = models.CharField(max_length=100)
    symptoms = models.CharField(max_length=100)
    chronic = models.CharField(max_length=100)

class DiagnosticsDesc(models.Model):
    diagnosticsDescId = models.CharField(max_length=8, primary_key=True)
    cause = models.TextField()
    symptomsDesc = models.TextField()

class Diagnostics(models.Model):
    diagnosticsId = models.CharField(max_length=8, primary_key=True)
    treatmentId = models.ForeignKey(Treatment, on_delete=models.CASCADE)
    sicknessId = models.ForeignKey(Sickness, on_delete=models.CASCADE)
    diagnosticsDescId = models.ForeignKey(DiagnosticsDesc, on_delete=models.CASCADE)
    doctorId = models.ForeignKey(Doctor, on_delete=models.CASCADE)

class SergicalRecord(models.Model):
    sergicalRecordId = models.CharField(max_length=8, primary_key=True)
    sergType = models.CharField(max_length=50)
    progressReport = models.TextField(max_length=5000)
    operationDate = models.DateTimeField()
    doctorId = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    diagnosticsId = models.ForeignKey(Diagnostics, on_delete=models.CASCADE)

class PregnancyComplications(models.Model):
    complicationId = models.CharField(max_length=8, primary_key=True)
    complication = models.CharField(max_length=100)
    description = models.TextField()

class ObstericsRecord(models.Model):
    obstericRecordId = models.CharField(max_length=8, primary_key=True)
    pregnancies = models.IntegerField()
    complicationId = models.ForeignKey(PregnancyComplications, on_delete=models.CASCADE)
    date = models.DateTimeField()
    doctorId = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    diagnosticsId = models.ForeignKey(Diagnostics, on_delete=models.CASCADE)

class Allergies(models.Model):
    allergiesId = models.CharField(max_length=8, primary_key=True)
    symptoms = models.CharField(max_length=250)
    diagnosticsId = models.ForeignKey(Diagnostics, on_delete=models.CASCADE)

class Exam(models.Model):
    examId = models.CharField(max_length=8, primary_key=True)
    examType = models.CharField(max_length=250)
    date = models.DateTimeField()
    doctorId = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    diagnosticsId = models.ForeignKey(Diagnostics, on_delete=models.CASCADE)

class MedRecords(models.Model):
    diagnosticsId = models.ForeignKey(Diagnostics, on_delete=models.CASCADE)
    sergicalRecordId = models.ForeignKey(SergicalRecord, on_delete=models.CASCADE)
    obstrericId = models.ForeignKey(ObstericsRecord, on_delete=models.CASCADE)
    allergiesId = models.ForeignKey(Allergies, on_delete=models.CASCADE)
    examsId = models.ForeignKey(Exam, on_delete=models.CASCADE)

class Address(models.Model):
    addressId = models.CharField(max_length=8, primary_key=True)
    country = models.CharField(max_length=65)
    province = models.CharField(max_length=65)
    city = models.CharField(max_length=65)
    zipCode = models.CharField(max_length=65)
    addressLine1 = models.CharField(max_length=200)
