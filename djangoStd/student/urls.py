from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('', views.get_redirect),
    path('list/', views.major_list, name='list'),
    path('<pk>/detail/', views.major_detail, name='detail'),
    # path('new/', views.majorlist, name='new'),
    # path('delete/', views.majorlist, name='del'),
    # path('update/', views.majorlist, name='update'),
]