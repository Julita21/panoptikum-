from django.shortcuts import render


from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from talk.models import Post
from talk.serializers import PostSerializer


@api_view(['GET'])
def post_collection(request):
    if request.method == "GET":
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

@api_view(["GET", "POST"])
def post_element(request, pk):
    if request.method == "GET":
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

# GET api/v1/posts
# POST api/v1/posts
class PostCollection(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostMember(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
