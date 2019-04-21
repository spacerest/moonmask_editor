from rest_framework import serializers
from .models import Artwork

class artworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artwork
        image = serializers.ImageField(max_length = None, use_url = True)
        fields = (
            'title',
            'image',
            'author',
            'moonRelativeDate',
            'moonDate',
            'mainImageUrl',
            'mainImageInstagramUrl',
            'mainImageColor',
            'maskPositiveSpaceUrl',
            'maskPositiveSpaceInstagramUrl',
            'maskPositiveSpaceColor',
            'maskNegativeSpaceUrl',
            'maskNegativeSpaceInstagramUrl',
            'maskNegativeSpaceColor',
            'negativeSpaceTransparency',
            'positiveSpaceTransparency',
            'dimensionality',

        )
