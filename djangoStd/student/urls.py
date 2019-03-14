from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('', views.index, name='index'),

    path('major/list/', views.major_list, name='mj_list'),
    path('<pk>/major/detail/', views.major_detail, name='mj_detail'),
    path('major/new/', views.major_new, name='mj_new'),
    path('<pk>/major/delete/', views.major_del, name='mj_del'),
    path('<pk>/major/update/', views.major_update, name='mj_update'),

    path('std/list/', views.student_list, name="std_list"),
    path('<pk>/std/detail/', views.student_detail, name="std_detail"),
    path('std/new/', views.student_new, name='std_new'),
    path('<pk>/std/delete/', views.student_del, name="std_del"),
    path('<pk>/std/update/', views.student_update, name="std_update"),

    path('searchMajor/', views.searchMajor),
    path('searchStudent/', views.searchStudent),
]