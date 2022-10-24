from rest_framework.routers import DefaultRouter
from APP.Doctor.views import DoctorsViewSet


router_doctors = DefaultRouter()

router_doctors.register(prefix='doctors', basename='doctors', viewset=DoctorsViewSet)