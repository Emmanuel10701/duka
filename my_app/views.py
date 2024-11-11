from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from .models import Post
from .serializers import Postserilizer

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = Postserilizer
    permission_classes = [AllowAny]  

    def perform_create(self, serializer):
        serializer.save()

class PostRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = Postserilizer
    permission_classes = [AllowAny]  # No restrictions on viewing or updating posts

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views += 1  # Increment views count
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = Postserilizer
    permission_classes = [AllowAny]  # No restrictions on viewing details

class PostDestroyView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = Postserilizer
    permission_classes = [AllowAny]  # No restrictions on deleting posts

    def perform_destroy(self, instance):
        instance.delete()
