from django.db.models import Model, DateTimeField, CharField, TextField, BooleanField
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([item[1][0], item[0]] for item in LEXERS)
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(Model):
    title = CharField(max_length=100, blank=True, default="")
    code = TextField()
    linenos = BooleanField(default=False)
    language = CharField(max_length=100, default="python", choices=LANGUAGE_CHOICES)
    style = CharField(max_length=100, default="friendly", choices=STYLE_CHOICES)
    created = DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created"]
