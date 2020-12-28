from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import PatientViewSet, DoctorViewSet, AddressViewset, MedRecordsViewSet, DiagnosticsViewset, TreatmentViewset, SicknesViewset, PrescriptionViewset, DiagnosticsDescViewset, AllergiesViewset, SergicalRecordViewset, ObstericsRecordViewset, ExamViewset

router = routers.DefaultRouter()
router.register('patients', PatientViewSet)
router.register('doctors', DoctorViewSet)
router.register('address', AddressViewset)
router.register('medrecords', MedRecordsViewSet)
router.register('diagnostics', DiagnosticsViewset)
router.register('treatment', TreatmentViewset)
router.register('sickness', SicknesViewset)
router.register('prescription', PrescriptionViewset)
router.register('diagnostics-description', DiagnosticsDescViewset)
router.register('allergies', AllergiesViewset)
router.register('sergical-record', SergicalRecordViewset)
router.register('obsterics-record', ObstericsRecordViewset)
router.register('exam', ExamViewset)

urlpatterns = [
    path('', include(router.urls)),
]
