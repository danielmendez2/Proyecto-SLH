from rest_framework.routers import DefaultRouter
from APP.License.views import VaccinesModelViewSet, Growth_and_developmentModelViewSet


router_vaccines = DefaultRouter()

router_vaccines.register(prefix='vaccines', basename='vaccines', viewset=VaccinesModelViewSet)

router_growth = DefaultRouter()

router_growth.register(prefix='growth_and_development', basename='growth_and_development',
                       viewset=Growth_and_developmentModelViewSet)