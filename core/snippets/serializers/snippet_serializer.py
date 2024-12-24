from rest_framework.serializers import ModelSerializer

from core.snippets.models import Snippet


class SnippetSerializer(ModelSerializer):
    class Meta:
        model = Snippet
        fields = ["id", "title", "code", "linenos", "language", "style"]
