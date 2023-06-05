from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'account'
urlpatterns = [
    path('signup/', views.student_signup_view, name="signup"),
    path('login/', views.login_view, name="login"),
     path('school_signup/', views.institution_signup_view, name="school_signup"),
    path('school_login/', views.login_view, name="school_login"),
     path('sponsor_signup/', views.institution_signup_view, name="sponsor_signup"),
    path('sponsor_login/', views.login_view, name="sponsor_login"),
    path('logout/', views.logout_view, name="logout"),
    path('authenticate/', views.first_page_view, name="authenticate"),
    path('le_projet/', views.project_view, name="projet"),
    path('a_propos/', views.purpose_view, name="propos"),
    path('agir_avec_nous/', views.act_view, name="agir"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)