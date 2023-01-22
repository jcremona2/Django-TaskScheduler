"""CRUD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks import views as taskview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', taskview.home, name='home'),
    path('signup/', taskview.signup, name='signup'),
    path('logout/',taskview.signout, name= 'logout'),
    path('signin/',taskview.signin, name='singin'),
    path('tasks/',taskview.tasks, name='tasks'),
    path('tasks/completed',taskview.tasks_completed, name='tasks_completed'),
    path('tasks/create/',taskview.create_task,name='create_task'),
    path("task/<int:task_id>/", taskview.task_detail, name="task_detail"),
    path("task/<int:task_id>/complete", taskview.task_complete, name="task_complete"),
    path("task/<int:task_id>/delete", taskview.task_delete, name="task_delete")
]
