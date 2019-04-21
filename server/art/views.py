from rest_framework import generics, mixins
from .models import Artwork
from .serializers import artworkSerializer
from rest_framework.permissions import IsAuthenticated

class artworkAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    #permission_classes = (IsAuthenticated, )
    resource_name = 'artwork'
    serializer_class = artworkSerializer

    def get_queryset(self):
        return Artwork.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class artworkRudView(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (IsAuthenticated, )
    resource_name = 'artwork'
    lookup_field = 'id'
    serializer_class = artworkSerializer

    def get_queryset(self):
        return Artwork.objects.all()
