from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from core.snippets.models import Snippet
from core.snippets.serializers import SnippetSerializer


@csrf_exempt
def snippet_detail(request, pk):
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = SnippetSerializer(instance=snippet)
        return JsonResponse(data=serializer.data)

    elif request.method == "DELETE":
        snippet.delete()
        return HttpResponse(status=204)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(instance=snippet, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)

        return JsonResponse(data=serializer.errors, status=400)
