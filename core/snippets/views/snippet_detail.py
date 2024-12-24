from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
)

from core.snippets.models import Snippet
from core.snippets.serializers import SnippetSerializer


@api_view(http_method_names=["GET", "DELETE", "PUT"])
def snippet_detail(request, pk):
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = SnippetSerializer(instance=snippet)
        return Response(data=serializer.data)

    elif request.method == "DELETE":
        snippet.delete()
        return Response(status=HTTP_204_NO_CONTENT)

    elif request.method == "PUT":
        serializer = SnippetSerializer(instance=snippet, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)

        return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)
