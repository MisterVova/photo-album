from rest_framework import viewsets
from photo_albums.api.v1.serializers import PhotoSerializer, Photo


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
