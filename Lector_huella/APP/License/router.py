from rest_framework.routers import DefaultRouter
from APP.License.views import VaccinesViewSet, Growth_and_developmentViewSet


router_vaccines = DefaultRouter()

router_vaccines.register(prefix='vaccines', basename='vaccines', viewset=VaccinesViewSet)

router_growth = DefaultRouter()

router_growth.register(prefix='growth_and_development', basename='growth_and_development',
                       viewset=Growth_and_developmentViewSet)