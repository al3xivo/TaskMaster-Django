from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('task/', views.task_view, name='task'), #Onde fica as tarefas adicionadas
    path('register/', views.register_view, name='register'), #Registrar acc
    path('taskregister/', views.task_register, name='taskregister'), #Criar uma tarefa
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'), #editar a tarefa
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'), #apagar a tarefa
]
