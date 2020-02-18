from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "prof"
urlpatterns = [
    path('<int:prof_id>', views.Detail, name='detail')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)