from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('signup/', views.register,name="signup"),
    path('login/', views.user_login,name="login"),
    path('todopage/', views.todopage,name="todopage"),
    path('logout/', views.user_logout,name="logout"),
    
]