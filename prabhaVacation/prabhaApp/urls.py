
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index ),
    path("main", views.index ),
    path("branches", views.branches),
    path("contact_us", views.contacts),
    path("about_us", views.about),
    path("vacation_plans", views.vacations),
    path("vacation_form", views.forms)
]
