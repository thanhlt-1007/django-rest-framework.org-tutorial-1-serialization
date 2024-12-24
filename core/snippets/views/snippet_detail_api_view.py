from django.http import Http404
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
)
from rest_framework.views import APIView

from core.snippets.models import Snippet
from core.snippets.serializers import SnippetSerializer


class SnippetDetailApiView(APIView):
    def _get_snippet(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self._get_snippet(pk=pk)
        serializer = SnippetSerializer(instance=snippet)
        return Response(data=serializer.data)

    def delete(self, request, pk, format=None):
        snippet = self._get_snippet(pk=pk)
        snippet.delete()
        return Response(status=HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        snippet = self._get_snippet(pk=pk)
        serializer = SnippetSerializer(instance=snippet, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)

        return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)
