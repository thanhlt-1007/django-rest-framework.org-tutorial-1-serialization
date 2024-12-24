from django.urls import path

from core.snippets.views import snippet_list

urlpatterns = [
    path("snippets/", snippet_list),
]
