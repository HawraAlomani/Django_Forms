from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.project, name='project'),
    path('form/', views.form_example, name="form_example")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
