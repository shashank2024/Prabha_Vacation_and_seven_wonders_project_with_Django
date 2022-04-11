from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:wonder>", views.wonder_details_by_number),
    path("<str:wonder>", views.wonder_details, name="wonders_in_detail")
]