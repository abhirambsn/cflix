from django.shortcuts import render
from django.template import RequestContext

# Create your views here.

def h404(request,exception):
    response = render(request, 'errors/404.html', context_instance=RequestContext(request))
    response.status_code = 404
    return response

def h500(request):
    response = render(request, 'errors/404.html', context={})
    response.status_code = 500
    return response