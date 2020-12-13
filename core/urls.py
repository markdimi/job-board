from django.urls import path
from . import views

urlpatterns = [
    path('', views.JobView.as_view(), name='Donestreet job board')
]