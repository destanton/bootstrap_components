from django.shortcuts import render
from app.models import Song


def index_view(request):
    context = {
        "song": Song.objects.all(),
    }
    return render(request, "index.html", context)


def album_info(request, row_id):
    context = {
        # "album": Song.object.filter(album=album),
        "song": Song.objects.get(id=row_id)


    }
    return render(request, "album.html", context)


def about_info(request):

    return render(request, "about.html")
