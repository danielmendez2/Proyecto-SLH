from rest_framework.routers import DefaultRouter
from APP.clinic_history.views import HistoryModelViewSet


router_history = DefaultRouter()

router_history.register(prefix='history', basename='history', viewset=HistoryModelViewSet)
