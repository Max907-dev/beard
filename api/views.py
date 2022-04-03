from api.custom_renderes import JPEGRenderer
from rest_framework import generics
from images.models import Images
from rest_framework.response import Response


class ImageAPIView(generics.RetrieveAPIView):

    queryset = Images.objects.filter(id=1)
    renderer_classes = [JPEGRenderer]

    def get(self, request, *args, **kwargs):
        queryset = Images.objects.get(id=self.kwargs['id']).image
        data = queryset
        return Response(data, content_type='image/jpg')
