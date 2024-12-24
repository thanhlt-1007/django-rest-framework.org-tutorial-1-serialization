from django.urls import path

from core.snippets.views import SnippetDetailApiView, SnippetListApiView

urlpatterns = [
    path("snippets/", SnippetListApiView.as_view()),
    path("snippets/<int:pk>/", SnippetDetailApiView.as_view()),
]
