from django.urls import path
from . import views

app_name = "prof"
urlpatterns = [
    path('<int:prof_id>', views.Detail, name='detail')
]