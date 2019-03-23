from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
# from ..users.views import register_view
import os
os.sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from users.views import register_view


urlpatterns = [
    path('', include('boat.urls')),
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('login/', views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)