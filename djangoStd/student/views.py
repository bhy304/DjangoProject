from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Major, Student

# Create your views here.

def get_redirect(request):
    return redirect("list/") 

major_list = ListView.as_view(model=Major, template_name='student/majorlist.html')
major_detail = DetailView.as_view(model=Major, template_name='student/majordetail.html')
major_new = CreateView.as_view(model=Major, template_name='student/majorform.html', fields='__all__')
major_update = UpdateView.as_view(model=Major, template_name='student/majorform.html', fields='__all__')
major_del = DeleteView.as_view(model=Major, template_name='student/major_confirm_delete.html', success_url='/student/')

student_list = ListView.as_view(model=Student, template_name='student/studentlist.html')