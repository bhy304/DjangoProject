from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Major, Student
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

# Major, Student를 이용한 CRUD TEST

# def get_redirect(request):
#     return redirect("major/list/") 

def index(request):
    main = Student.objects.all()
    return render(request, 'student/index.html',{'index':main})

major_list = ListView.as_view(model=Major, template_name='student/majorlist.html')
major_detail = DetailView.as_view(model=Major, template_name='student/majordetail.html')
major_new = CreateView.as_view(model=Major, template_name='student/majorform.html', fields='__all__')
major_update = UpdateView.as_view(model=Major, template_name='student/majorform.html', fields='__all__')
major_del = DeleteView.as_view(model=Major, template_name='student/major_confirm_delete.html', success_url='/student/major/list/')

student_list = ListView.as_view(model=Student, template_name='student/studentlist.html')
student_detail = DetailView.as_view(model=Student, template_name='student/studentdetail.html')
student_new = CreateView.as_view(model=Student, template_name='student/studentform.html', fields='__all__')
student_update = UpdateView.as_view(model=Student, template_name='student/studentform.html', fields='__all__')
student_del = DeleteView.as_view(model=Student, template_name='student/student_confirm_delete.html', success_url='/student/std/list/')

#Major_Ajax : major_id로 검색
@csrf_exempt
def searchMajor(request):
    data = request.POST['major_id']
    search = Major.objects.filter(major_title__contains = data)
    print(search)

    return render(request, 'student/majorlist2.html', {'major_list':search})

#Student_Ajax : name 으로 검색
@csrf_exempt
def searchStudent(request):
    data = request.POST['name']
    search = Student.objects.filter(name__contains = data)
    print(search)

    return render(request, 'student/studentlist2.html', {'student_list':search})