from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Major, Student
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import pymysql 
import pandas as pd
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Major, Student를 이용한 CRUD TEST

# Index Page
def index(request):
    main = Student.objects.all()
    return render(request, 'student/index.html',{'index':main})

# Major
major_list = ListView.as_view(model=Major, template_name='student/majorlist.html')
major_detail = DetailView.as_view(model=Major, template_name='student/majordetail.html')
major_new = CreateView.as_view(model=Major, template_name='student/majorform.html', fields='__all__')
major_update = UpdateView.as_view(model=Major, template_name='student/majorform.html', fields='__all__')
major_del = DeleteView.as_view(model=Major, template_name='student/major_confirm_delete.html', success_url='/student/major/list/')

# Student
student_list = ListView.as_view(model=Student, template_name='student/studentlist.html')
student_detail = DetailView.as_view(model=Student, template_name='student/studentdetail.html')
student_new = CreateView.as_view(model=Student, template_name='student/studentform.html', fields='__all__')
student_update = UpdateView.as_view(model=Student, template_name='student/studentform.html', fields='__all__')
student_del = DeleteView.as_view(model=Student, template_name='student/student_confirm_delete.html', success_url='/student/std/list/')

# Major_Ajax : major_id로 검색
@csrf_exempt
def searchMajor(request):
    data = request.POST['major_id']
    search = Major.objects.filter(major_title__contains = data)
    print(search)

    return render(request, 'student/majorlist2.html', {'major_list':search})

#Student_Ajax : name 으로 검색
@csrf_exempt
def searchStudent(request):
    '''data = request.POST['name']
    search = Student.objects.filter(name__contains = data)'''
    data = request.POST['major']
    search = Student.objects.filter(major__major_title__contains = data)
    print(search)

    return render(request, 'student/studentlist2.html', {'student_list':search})

# Major_DB 삭제
def deleteMajor(request):
    db = pymysql.connect(host="localhost",user="root",password="1234",db="student",charset="utf8")
    cur = db.cursor()
    sql = "delete from student_major"
    cur.execute(sql)
    db.commit()
    db.close()
    print("DONE")
    return render(request, 'student/majorlist.html')

# Student_DB 삭제
def deleteStudent(request):
    db = pymysql.connect(host="localhost",user="root",password="1234",db="student",charset="utf8")
    cur = db.cursor()
    sql = "delete from student_student"
    cur.execute(sql)   
    db.commit()
    db.close()
    print("DONE")
    return render(request, 'student/studentlist.html')

# Major_DB 삽입
def insertMajor(request):
    db = pymysql.connect(host="localhost",user="root",password="1234",db="student",charset="utf8")
    cur = db.cursor()
    csv_data = pd.read_csv('csv/major.csv')
    sql = 'INSERT INTO student_major(major_id, major_title) values(%s, %s)'
    print(sql)
    for row in csv_data.get_values():
        cur.execute(sql, tuple(row))
    db.commit()
    db.close()
    return render(request, 'student/majorlist.html')

# Student_DB 삽입
def insertStudent(request):
    # DB 연결
    db = pymysql.connect(host="localhost",user="root",password="1234",db="student",charset="utf8")
    # 커서 생성
    cursor = db.cursor()
    # csv 읽어오기
    csv_data = pd.read_csv('csv/student.csv')
    csv_data = csv_data.fillna("")
    #csv_data
    sql = """INSERT INTO student_student(studentID, name, major_id, phone, address, hobby, skill) 
             values(%s, %s, %s, %s, %s, %s, %s)"""

    for row in csv_data.get_values():
        cursor.execute(sql, tuple(row))
        print(row)
    db.commit()
    db.close()
    return render(request, 'student/studentlist.html')

#csvToDB : DB 삽입
# def insertData(request):
#     data_type = request.POST.get('data_type')
#     if request.method == 'POST' and data_type == 'major':
#         uploaded_file = request.FILES['upload']
            
#         db = pymysql.connect(host="localhost",user="root",password="1234",db="student",charset="utf8")
#         cur = db.cursor()
#         csv_data = pd.read_csv(uploaded_file)
#         sql = 'INSERT INTO student_major(major_id, major_title) values(%s, %s)'
#         print(sql)
#         for row in csv_data.get_values():
#             cur.execute(sql, tuple(row))
#         db.commit()
#         db.close()
#         return render(request,'student/majorlist.html')