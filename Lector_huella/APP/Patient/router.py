from rest_framework.routers import DefaultRouter
from APP.Patient.views import PatientsModelViewSet


router_patients = DefaultRouter()

router_patients.register(prefix='patients', basename='patients', viewset=PatientsModelViewSet)