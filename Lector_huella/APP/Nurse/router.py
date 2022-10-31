from rest_framework.routers import DefaultRouter
from APP.Nurse.views import NurseViewSet


router_nurse = DefaultRouter()

router_nurse.register(prefix='nurse', basename='nurse', viewset=NurseViewSet)