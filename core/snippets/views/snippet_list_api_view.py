from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin

from core.snippets.models import Snippet
from core.snippets.serializers import SnippetSerializer


class SnippetListApiView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
