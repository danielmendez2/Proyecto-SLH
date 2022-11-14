"""Lector_huella URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from APP.user.routers import router_user
from APP.Patient.router import router_patients
from APP.Doctor.routers import router_doctors
from APP.clinic_history.router import router_history
from APP.License.router import router_vaccines, router_growth
from APP.Nurse.router import router_nurse

class Protegida(ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        return Response({"content": "Esta vista es segura"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', jwt_views.TokenRefreshView.as_view(),name='token_refresh'),
    #path('api/historia/lista', HistoriaListAPIView.as_view(), name='historia'),
    path('api/user', include(router_user.urls)),
    path('api/Patients', include(router_patients.urls)),
    path('api/Doctors',include(router_doctors.urls)),
    path('api/history',include(router_history.urls)),
    path('api/Vaccines',include(router_vaccines.urls)),
    path('api/Growth', include(router_growth.urls)),
    path('api/nurse', include(router_nurse.urls)),
]