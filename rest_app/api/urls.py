from django.conf.urls import url
from rest_app.api.views import ListCreateCasinos, DetailAPIView

urlpatterns = [
   url(r'^$', ListCreateCasinos.as_view(), name='list_casino'),
#   url(r'^create$', CreateAPIView.as_view(), name='create_casino'),
   url(r'^(?P<pk>\d+)/$', DetailAPIView.as_view(), name='detail_casino'),
]
