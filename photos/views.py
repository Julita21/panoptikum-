from django.shortcuts import render

# Create your views here.
from photos.models import Gallery


def gallery_list(request):
    galleries = Gallery.objects.all()

    return render(
        request,
        "photos/list.html",
        {"galleries": galleries}
    )

def gallery_details(request, id):
    gallery = Gallery.objects.get(pk=id)

    return render(
        request,
        "photos/details.html",
        {"gallery": gallery}
    )