from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Department, Doctors

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def booking(request):
    return render(request, 'booking.html')
def doctors(request):
    return render(request, 'doctors.html')

def contact(request):
    return render(request, 'contact.html')
def department(request):
    return render(request, 'department.html')

