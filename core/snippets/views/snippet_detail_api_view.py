from rest_framework.generics import RetrieveUpdateDestroyAPIView

from core.snippets.models import Snippet
from core.snippets.serializers import SnippetSerializer


class SnippetDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
