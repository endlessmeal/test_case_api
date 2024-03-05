from django.urls import path, include

urlpatterns = [
    path('admin/', include('admin.urls')),
    path('api/', include('app.urls')),
]
