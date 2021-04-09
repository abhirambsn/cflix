from django.urls import path
from .views import getVideo

urlpatterns = [
    path('<str:video_id>/', getVideo, name="video")
]