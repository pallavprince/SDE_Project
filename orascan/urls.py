from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('scan', views.home, name='scan'),
    path('history/', views.history, name='history'),
    path('history/<str:id>/', views.scan_history, name='history'),
]
