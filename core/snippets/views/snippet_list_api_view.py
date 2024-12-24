from rest_framework.generics import ListCreateAPIView

from core.snippets.models import Snippet
from core.snippets.serializers import SnippetSerializer


class SnippetListApiView(ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
