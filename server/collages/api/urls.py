from .views import collageAPIView, collageRudView
from django.conf.urls import url
from django.urls import path, include

app_name = 'collages'

urlpatterns = [
    url(r'^$', collageAPIView.as_view(), name='collage-create'),
    url('(?P<id>\d+)', collageRudView.as_view(), name='collage-rud'),
    path('rest-auth/', include('rest_auth.urls'))
]
