from django.urls import path
from .views import loginUser, logoutUser, home, profile, dashboard, registerUser, settings, search, videos, music

app_name="main"
urlpatterns = [
    path('', home, name="home"),
    path('login/', loginUser, name="login"),
    path('logout/', logoutUser, name="logout"),
    path('register/', registerUser, name="register"),
    path('dashboard/', dashboard, name="dash"),
    path('search/', search, name="search"),
    path('video/', videos, name="videos"),
    path('audio/', music, name="music"),
    path('settings/', settings, name="settings"),
    path('profile/', profile, name="profile"),
]
