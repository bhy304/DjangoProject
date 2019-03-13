from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('', views.index),
    path('list/', views.major_list, name='list'),
    # path('detail/', views.majorlist, name='detail'),
    # path('new/', views.majorlist, name='new'),
    # path('delete/', views.majorlist, name='del'),
    # path('update/', views.majorlist, name='update'),
]