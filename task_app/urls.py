from django.urls import path
from . import views


app_name = "task_app"

urlpatterns = [
    path("home/", views.home, name="home"),
    # path('create/<int:task_id>/', views.edit_task, name='edit_task'),
    path('update/<int:task_id>/', views.update_task, name='update_task'),
    path('confirm-delete/<int:task_id>/', views.confirm_delete_task, name='confirm_delete_task'),
    path('views/', views.views_by_task, name='views_by_task'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add/', views.add_task, name='add_task'),
    path('task_detail/<int:task_id>/', views.task_detail, name='task_detail'),
    #  path('task_list', views.task_list, name='task_list'),
    #  path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    # path('tasks/todo/', views.todo_tasks, name='todo_tasks'),
    # path('tasks/inprogress/', views.inprogress_tasks, name='inprogress_tasks'),
    # path('tasks/complete/', views.complete_tasks, name='complete_tasks'),
]