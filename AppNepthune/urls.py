from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'AppNepthune'
urlpatterns = [
    path('', views.index, name='index'),
    path('modif-infos-persos.html', views.infos_perso, name='infos'),
    path('AppNepthune/<int:student_id>/', views.detail, name='detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)