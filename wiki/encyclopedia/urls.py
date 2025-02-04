from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>",views.entry_page,name="entry_page"),
    path("Search_bar/",views.Search_bar,name="Search_bar"),
    path('new_page/',views.new_page,name='new_page'),
    path("edit_page/",views.edit_page,name="edit_page"),
    path("save_edit/",views.save_edit,name="save_edit"),
    path("random_page/",views.random_page,name="random_page")
]