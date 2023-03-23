from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'account'
urlpatterns = [
    path('signup/', views.signup_view, name="signup"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('authenticate/', views.first_page_view, name="authenticate"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)