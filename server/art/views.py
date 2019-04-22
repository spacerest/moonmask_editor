from rest_framework import generics, mixins
from .models import Artwork
from .serializers import artworkSerializer
from rest_framework.permissions import IsAuthenticated

class artworkAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    #permission_classes = (IsAuthenticated, )
    resource_name = 'artworks'
    serializer_class = artworkSerializer

    def get_queryset(self):
        return Artwork.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class artworkUpdateAPIView(mixins.UpdateModelMixin, generics.ListAPIView):
    resource_name = 'artworks'
    serializer_class = artworkSerializer

    def post(self, request, *args, **kwargs):
        return self.save(request, *args, **kwargs)

class artworkRudView(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (IsAuthenticated, )
    resource_name = 'artworks'
    lookup_field = 'id'
    serializer_class = artworkSerializer

    def get_queryset(self):
        return Artwork.objects.all()
