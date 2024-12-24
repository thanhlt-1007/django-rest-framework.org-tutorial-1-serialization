from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    DestroyModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)

from core.snippets.models import Snippet
from core.snippets.serializers import SnippetSerializer


class SnippetDetailApiView(
    GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
