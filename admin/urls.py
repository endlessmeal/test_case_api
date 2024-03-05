from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, PointOfSaleViewSet, VisitViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet, basename='employee')
router.register(r'points_of_sale', PointOfSaleViewSet, basename='point_of_sale')
router.register(r'visits', VisitViewSet, basename='visit')


urlpatterns = [
    path('', include(router.urls)),
]
