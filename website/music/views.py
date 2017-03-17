from django.shortcuts import render
from django.http import Http404
from .models import Album
from django.shortcuts import render


# Create your views here.
def index(request):
    all_album = Album.objects.all()
    context = {
        'all_album' : all_album,
    }
    return render(request,'music/index.html',context)

def details(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
        context = {
            'album': album,
        }
    except Album.DoesNotExist:
        raise Http404("No such album")
    return render(request,'music/details.html',context)