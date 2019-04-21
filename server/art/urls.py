from .views import artworkAPIView, artworkRudView
from django.conf.urls import url
from django.urls import path, include

app_name = 'art'

urlpatterns = [
    url(r'^$', artworkAPIView.as_view(), name='artwork-create'),
    url('(?P<id>\d+)', artworkRudView.as_view(), name='artwork-rud'),
    path('rest-auth/', include('rest_auth.urls'))
]
