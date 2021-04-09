from django.urls import path
from .views import getAudio

urlpatterns = [
    path('<str:audio_id>/', getAudio, name="audio")
]