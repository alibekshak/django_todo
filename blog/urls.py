from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("add/", views.add_todo, name="add"),
    path("complete/<todo_id>", views.complete_todo, name="complete"),
    path("delete_completed", views.delete_completed, name="deletecompleted"),
    path("delete_all", views.delete_all, name='deleteall'),
    path("add_form", views.add_form),
]