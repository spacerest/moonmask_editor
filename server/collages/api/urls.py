from .views import collageAPIView, collageRudView
from django.conf.urls import url

app_name = 'collages'

urlpatterns = [
    url(r'^$', collageAPIView.as_view(), name='collage-create'),
    url('(?P<id>\d+)', collageRudView.as_view(), name='collage-rud')
]
