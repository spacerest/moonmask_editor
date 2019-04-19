from rest_framework import generics, mixins
from collages.models import Collage
from .serializers import collageSerializer

class collageAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    resource_name = 'collages'
    serializer_class = collageSerializer

    def get_queryset(self):
        return Collage.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
