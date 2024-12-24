from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from core.snippets.models import Snippet
from core.snippets.serializers import SnippetSerializer


@csrf_exempt
def snippet_list(request):
    if request.method == "GET":
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(instance=snippets, many=True)
        return JsonResponse(data=serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parser(request)
        serializer = SnippetSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=201)

        return JsonResponse(data=serializer.errors, status=400)
