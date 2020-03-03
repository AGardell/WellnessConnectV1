from django.urls import path
from . import views

app_name = "user"
urlpatterns = [
    path('login/', views.Login, name='login'),
    path('signup/', views.Signup, name='signup'),
    path('logout/', views.Logout, name='logout')
]