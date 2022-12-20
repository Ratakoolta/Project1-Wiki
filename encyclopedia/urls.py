from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search/", views.search, name="search"),
    path("add/", views.add_article, name="add_article"),
    path("edit/", views.edit_article, name="edit_article"),
    path("save/", views.save_edit, name="save_edit"),
]
