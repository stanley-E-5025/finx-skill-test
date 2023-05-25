from django.urls import path
from . import views

urlpatterns = [
    path('user/<str:name>', views.user_details)
]
