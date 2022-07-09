# tasks.urls.py

from django.urls import path, include

from tasks import views

app_name = 'tasks'
urlpatterns = [
    path(
        route='',
        view=views.index_view,
        name='collections'
    ),
    path('collection/', include([
        path(
            route='add/',
            view=views.create_collection,
            name='create_collection'
        ),
        path(
            route="<pk>/delete/",
            view=views.delete_collection,
            name='delete_collection'
        ),
        path(
            route="<pk>/tasks/",
            view=views.get_tasks,
            name='get_tasks'
        ),
    ])),

    path('collection/task/', include([
        path(
            route="add/",
            view=views.create_task,
            name='create_task'
        ),
        path(
            route="<pk>/delete/",
            view=views.delete_task,
            name='delete_task'
        ),
    ])),
]
