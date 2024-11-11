from rest_framework import serializers
from .models import Post

class Postserilizer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "_all_"
