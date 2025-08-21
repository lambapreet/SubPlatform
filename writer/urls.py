from django.urls import path
from . import views

urlpatterns = [
    path("writer-dashbaord/", views.writer_dashboard, name="writer-dashboard"),
]
