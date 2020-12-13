from rest_framework import serializers
from .models import Searches


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Searches
        fields = (
            'location', 'description', 'ip_address'
        )
