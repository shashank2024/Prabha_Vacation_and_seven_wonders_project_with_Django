from django.shortcuts import render

# Create your views here.

def index(request):
    return render (request, "prabhaApp/main.html")

def branches(request):
    return render (request, "prabhaApp/branches.html")

def contacts(request):
    return render (request, "prabhaApp/contact_us.html")

def about(request):
    return render (request, "prabhaApp/about_us.html")

def vacations(request):
    return render (request, "prabhaApp/vacation_plans.html")

def forms(request):
    return render (request, "prabhaApp/vacation_form.html")