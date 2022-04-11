from django.shortcuts import render

from django.views.generic import ListView

from bookmark.models import Bookmark


class BookmarkListView(ListView):
    model = Bookmark
    #bookmark_list.thml, {'bookmark_list': Bookmark.dbjects.all()}