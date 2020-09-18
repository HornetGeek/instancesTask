from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create_order , name="create"),
    path("stop", views.stop_order, name="stop")
]