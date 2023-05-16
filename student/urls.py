from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'student'
urlpatterns = [
    path('', views.index, name='index'),
    path('infos-persos.html', views.infos_perso, name='infos'),
    path('modif-infos-persos.html', views.modif_infos_perso, name='modif-infos'),
    path('<int:student_id>/', views.detail, name='detail'),
    path('myfilters.html', views.student_filters_view, name='filtres'),
    path('notifications.html', views.notifications_view, name='notifications'),
    #path("create", views)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

