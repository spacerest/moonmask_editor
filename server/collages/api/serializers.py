from rest_framework import serializers
from collages.models import Collage

class collageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collage
        fields = (
            'description',
            'image'
        )
