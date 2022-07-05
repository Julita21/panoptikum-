from django.urls import path

from talk.views import post_collection, post_element
from talk.views import PostCollection, PostMember

urlpatterns = [

    path("api/v1/posts/", post_collection),
    path("api/v1/posts/<pk>", post_element),
    path("api/v2/posts/", PostCollection.as_view()),
    path("api/v2/posts/<pk>", PostMember.as_view())
]