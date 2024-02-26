from django.shortcuts import render
from .models import Contentitem, Item  # Import Item model

# Create your views here.
app_name = 'web'

def index(request):
    context = {
        'name': "web",
        'Contentitems': Contentitem.objects.all(),
        'Items': Item.objects.all()  # Corrected assignment
    }
   
    return render(request, 'endex.html', context=context)


def application(environ, start_response):
    """
    Simple WSGI application.
    """
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)
    return [b"Hello, World! This is my Django WSGI application."]
