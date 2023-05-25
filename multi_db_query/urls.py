from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('user/<str:name>', views.user_details)
]
