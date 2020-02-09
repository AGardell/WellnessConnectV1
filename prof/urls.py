from django.urls import path
from . import views

app_name = "prof"
urlpatterns = [
    path('', views.Detail, name='detail')
]