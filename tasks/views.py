# tasks.views.py

from django.urls import reverse
from django.http import HttpResponse
from django.utils.html import escape
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404

from tasks.models import Collection, Task


def homePageView(request, template_name='tasks/_list.html'):

    context = {}

    collection_slug = request.GET.get("collection")

    if not collection_slug:
        collection = Collection.get_default_collection()
        return redirect(f"{reverse('tasks:collections')}?collection=_defaut")

    collection = get_object_or_404(Collection, slug=collection_slug)
    tasks = collection.task_set.order_by("description")

    collections = Collection.objects.order_by('name')

    context = {
        'tasks': tasks,
        'collection': collection,
        'collections': collections,
    }
    return render(request, template_name, context=context)


index_view = homePageView


def createCollectionView(request):

    collection_name = escape(request.POST.get('collection-name'))
    collection, created = Collection.objects.get_or_create(name=collection_name)

    if not created:
        return HttpResponse("Cette collection existe déjà !", status=409)

    context = {'collection': collection}
    template_name = 'tasks/partials/_collection.html'
    return render(request, template_name, context)


create_collection = createCollectionView


def deleteCollection(request, pk):
    collection = get_object_or_404(Collection, pk=pk)
    collection.delete()
    return redirect("tasks:collections")


delete_collection = deleteCollection


@csrf_exempt
def createTask(request):

    slug = request.POST.get("collection")
    collection = Collection.objects.get(slug=slug)
    description = escape(request.POST.get('task-description'))
    task = Task.objects.create(description=description, collection=collection)

    context = {'task': task}
    template_name = 'tasks/partials/_task.html'
    return render(request, template_name, context)


create_task = createTask


def deleteTask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return HttpResponse("")


delete_task = deleteTask


def getTasks(request, pk):

    collection = get_object_or_404(Collection, pk=pk)
    tasks = collection.task_set.order_by("description")

    context = {
        "tasks": tasks,
        "collection": collection
    }
    template_name = 'tasks/partials/tasks.html'
    return render(request, template_name, context)


get_tasks = getTasks
