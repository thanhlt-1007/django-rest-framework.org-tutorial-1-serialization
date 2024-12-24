from django.urls import path

from core.snippets.views import SnippetListApiView, snippet_detail

urlpatterns = [
    path("snippets/", SnippetListApiView.as_view()),
    path("snippets/<int:pk>/", snippet_detail),
]
