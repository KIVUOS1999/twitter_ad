from rest_framework  import serializers
from .models import *

class Get(serializers.Serializer):
    api_key = serializers.CharField(max_length = 100)
    api_secreat_key = serializers.CharField(max_length = 100)
    access_token = serializers.CharField(max_length = 100)
    access_token_secreat = serializers.CharField(max_length = 100)
    hashtag = serializers.CharField(max_length = 100)
    numbers = serializers.IntegerField()
    comment = serializers.CharField()

    def create(self, validated_data):
        return Data.objects.create(**validated_data)