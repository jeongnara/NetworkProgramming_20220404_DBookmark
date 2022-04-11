from django.urls import path

from bookmark.views import BookmarkListView

urlpatterns = [
    path('list/', BookmarkListView.as_view(), name='list')
]