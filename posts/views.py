from django.shortcuts import render

from django.shortcuts import render

# Create your views here.
from posts.models import Post


def post_list(request):
    posts = Post.objects.all()

    return render(
        request,
        "photos/list.html",
        {"posts": posts}
    )

def post_details(request, id):
    post = Post.objects.get(pk=id)

    return render(
        request,
        "photos/details.html",
        {"post": post}
    )
