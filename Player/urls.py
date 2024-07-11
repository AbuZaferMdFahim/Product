from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
#UI
from django.urls import path
urlpatterns = [
    path('check_player_profile/', views.check_player_profile, name='check_player_profile'),
    path('create_player_profile/', views.create_player_profile, name='create_player_profile'),
    path('player_profile/', views.player_profile, name='player_profile'),
    path('player_profile_create/', views.player_profile_create, name='player_profile_create'),
    path('addplayer_list/', views.addplayer_list, name='addplayer_list'),

] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) 
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
