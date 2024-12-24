from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

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
