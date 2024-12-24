from rest_framework.serializers import (
    BooleanField,
    CharField,
    ChoiceField,
    IntegerField,
    Serializer,
)

from core.snippets.models import LANGUAGE_CHOICES, STYLE_CHOICES, Snippet


class SnippetSerializer(Serializer):
    id = IntegerField(read_only=True)
    title = CharField(required=False, max_length=100, allow_blank=True)
    code = CharField(style={"base_template": "textarea.html"})
    linenos = BooleanField(required=False)
    language = ChoiceField(choices=LANGUAGE_CHOICES, default="python")
    style = ChoiceField(choices=STYLE_CHOICES, default="friendly")

    def create(self, validated_data):
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_date):
        instance.title = validated_date.get("title", instance.title)
        instance.code = validated_date.get("code", instance.code)
        instance.linenos = validated_date.get("linenos", instance.linenos)
        instance.language = validated_date.get("language", instance.language)
        instance.style = validated_date.get("style", instance.style)

        instance.save()
        return instance
