from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Major, Student

# Create your views here.

def index(request):
    return HttpResponse("Index")

major_list = ListView.as_view(model=Major)