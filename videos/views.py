from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Video

# Create your views here.

@login_required
def getVideo(request, video_id):
    vid = Video.objects.get(id=video_id)
    if vid is not None:
        return render(request, 'main/video.html', {'user': request.user, 'video': vid})
    return redirect('main:dash')

