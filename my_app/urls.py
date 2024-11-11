from django.urls import path
from .views import (
    PostListCreateView,
    PostRetrieveUpdateView,
    PostDetailView,
    PostDestroyView
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostRetrieveUpdateView.as_view(), name='post-retrieve-update'),
    path('posts/<int:pk>/detail/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/delete/', PostDestroyView.as_view(), name='post-delete'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)