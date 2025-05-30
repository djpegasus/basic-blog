from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path('register/', views.registerUser, name="register"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('dashboard/', views.dashboard, name="dashboard"),
]
