from django.urls import path
from . import views

urlpatterns = [
    path('points_of_sale/', views.get_points_of_sale, name='points_of_sale'),
    path('perform_visit/', views.perform_visit, name='perform_visit'),
]
