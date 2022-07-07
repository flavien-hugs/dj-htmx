# tasks.urls.py

from django.urls import path

from tasks import views

app_name='tasks'
urlpatterns = [
    path(
        route='',
        view=views.index_view,
        name='task_list'
    ),
    path(
        route='create/task/',
        view=views.create_collection,
        name='create_task'
    )
]
