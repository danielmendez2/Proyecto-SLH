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
from APP.clinic_history.views import HistoryViewSet
from APP.user.routers import router_user
from APP.Patient.router import router_patients
from APP.Doctor.routers import router_doctors
from APP.clinic_history.router import router_history
from APP.License.router import router_vaccines, router_growth
from APP.Nurse.router import router_nurse

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/historia/lista', HistoriaListAPIView.as_view(), name='historia'),
    path('api/user', include(router_user.urls)),
    path('api/Patients/list', include(router_patients.urls)),
    path('api/Doctors/list',include(router_doctors.urls)),
    path('api/history/list',include(router_history.urls)),
    path('api/Vaccines/list',include(router_vaccines.urls)),
    path('api/Growth/list', include(router_growth.urls)),
    path('api/nurse/list', include(router_nurse.urls)),
]
