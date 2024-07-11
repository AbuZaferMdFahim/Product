from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
#UI
from django.urls import path
urlpatterns = [
    path('check_manager_profile/', views.check_manager_profile, name='check_manager_profile'),
    path('create_manager_profile/', views.create_manager_profile, name='create_manager_profile'),
    path('manager_profile/', views.manager_profile, name='manager_profile'),
    path('manager_profile_create/', views.manager_profile_create, name='manager_profile_create'),

] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) 
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
