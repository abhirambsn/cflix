from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Music
# Create your views here.

@login_required
def getAudio(request, audio_id):
    mus = Music.objects.get(id=audio_id)
    if mus is not None:
        return render(request, 'main/audio.html', {'user': request.user, 'music': mus})
    return redirect('main:dash')
