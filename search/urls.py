from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "search"
urlpatterns = [
    path('', views.Index, name='index'),
    path('search/', views.Search, name='searchprof')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)