from rest_framework.routers import DefaultRouter
from APP.user.views import UserModelViewSet


router_user = DefaultRouter()

router_user.register(prefix='user', basename='user', viewset=UserModelViewSet)