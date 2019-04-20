from rest_framework import generics, mixins
from collages.models import Collage
from .serializers import collageSerializer
from rest_framework.permissions import IsAuthenticated

class collageAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    #permission_classes = (IsAuthenticated, )
    resource_name = 'collages'
    serializer_class = collageSerializer

    def get_queryset(self):
        return Collage.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class collageRudView(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (IsAuthenticated, )
    resource_name = 'collages'
    lookup_field = 'id'
    serializer_class = collageSerializer

    def get_queryset(self):
        return Collage.objects.all()
