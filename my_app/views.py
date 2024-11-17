from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from .models import Post
from .serializers import Postserilizer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings

class SendEmailAPI(APIView):
    def post(self, request):
        subject = 'Test Email'
        message = 'This is a test email sent from Django API.'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['recipient@example.com']  # Replace with a valid email address
        
        try:
            send_mail(subject, message, from_email, recipient_list)
            return Response({'message': 'Email sent successfully!'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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
