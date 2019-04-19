from .views import collageAPIView
from django.conf.urls import url

app_name = 'collages'

urlpatterns = [
    url('', collageAPIView.as_view(), name='collage-create'),
    #url('(?P<id\d+)', collageRudView.as_view(), name='collage-rud')
]
