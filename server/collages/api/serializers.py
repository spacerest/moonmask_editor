from rest_framework import serializers
from collages.models import Collage

class collageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collage
        image_url = serializers.SerializerMethodField('get_image_url')
        image = serializers.ImageField(max_length = None, use_url = True)
        fields = (
            'description',
            'image',
            'image_url'
        )

        def get_image_url(self, obj):
            return "hello"# obj.image.url
