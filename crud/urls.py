from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllTasksView, name = 'all_tasks'),
    path('delete_item/<int:pk>', views.DeleteTask, name = 'delete_task'),
    path('update_item<int:pk>', views.UpdateTask, name = 'update_task'),
]
