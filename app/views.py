from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import View,TemplateView
from app.forms import *
# Create your views here.


# FBV String response
def FBV_String(request):
    return HttpResponse('This is FBV String')

# CBV String response
class CBV_String(View):
    def get(self,request):
        return HttpResponse('This is CBV String')


# FBV html page render
def FBV_page(request):
    return render(request,'FBV_page.html')

# CBV html page render
class CBV_page(View):
    def get(self,request):
        return render(request,'CBV_page.html')

# data insertion
# FBV View
def FBV_insert(request):
    SFO = StudentForm()
    d={'SFO':SFO}
    if request.method == 'POST':
        SFDO = StudentForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Data inserted successfully')
    return render(request,'FBV_insert.html',d)

# Class View
class CBV_insert(View):
    def get(self,request):
        SFO = StudentForm()
        d={'SFO':SFO}
        return render(request,'CBV_insert.html',d)

    def post(self,request):
        SFDO = StudentForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Data inserted successfully')


# TemplateView class
class CBV_TempView(TemplateView):
    template_name = 'CBV_TempView.html'