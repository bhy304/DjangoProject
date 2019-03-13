from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('', views.get_redirect),
    path('list/', views.major_list, name='All_list'),
    path('<pk>/detail/', views.major_detail, name='detail'),
    path('new/', views.major_new, name='insert'),
    path('<pk>/delete/', views.major_del, name='del'),
    path('<pk>/update/', views.major_update, name='update'),

    path('stdlist/', views.student_list, name="student_list"),
]