# tasks.urls.py

from django.urls import path

from tasks import views

app_name = 'tasks'
urlpatterns = [
    path(
        route='',
        view=views.index_view,
        name='collections'
    ),
    path(
        route='add/collection/',
        view=views.create_collection,
        name='create_collection'
    ),
    path(
        route="add/collection/task/",
        view=views.create_task,
        name='create_task'
    ),
    path(
        route="collection/<pk>/get/tasks/",
        view=views.get_tasks,
        name='get_tasks'
    )
]
