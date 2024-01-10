from django.contrib import admin
from django.urls import path
from . import views
from .views import TaskListView, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, ListCreate

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.loginpage, name='login'),
    path('', TaskListView.as_view(), name='tasklistview'),
    path('logout/', views.logoutpage, name='logout'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('list-create/', ListCreate.as_view(), name='list-create'),
    path('create/', TaskCreate.as_view(), name='create'),
    path('update/<int:pk>/', TaskUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', TaskDelete.as_view(), name='delete'),


]

