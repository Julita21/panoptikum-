from django.urls import path

from photos.views import gallery_list, gallery_details

app_name = "photos"
urlpatterns = [
    path("/galleries/", gallery_list, name="list"),
    path("/galleries/<id>/", gallery_details, name="details"),
]