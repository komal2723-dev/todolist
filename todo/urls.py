from django.urls import path
# from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.register,name="signup"),
    path('login/', views.user_login,name="login"),
    path('todopage/', views.todopage,name="todopage"),
    path('logout/', views.user_logout,name="logout"),
    path('edit_todo/<int:task_id>', views.edit_todolist,name="edit_todo"),
    path('delete_todo/<int:task_id>', views.delete_task,name="delete_todo"),
    path('send-otp/', views.send_otp, name='send_otp'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('set_password/', views.set_password, name='set_password'),
]