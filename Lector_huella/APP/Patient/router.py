from rest_framework.routers import DefaultRouter
from APP.Patient.views import PatientsViewSet


router_patients = DefaultRouter()

router_patients.register(prefix='patients', basename='patients', viewset=PatientsViewSet)