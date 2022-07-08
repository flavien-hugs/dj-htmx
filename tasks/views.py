# tasks.views.py

from django.http import HttpResponse
from django.utils.html import escape
from django.shortcuts import render, redirect, get_object_or_404

from tasks.models import Collection, Task


def homePageView(request, template_name='tasks/_list.html'):

    context = {}

    collection_slug = request.GET.get("collection")
    collection = Collection.get_default_collection()

    if collection_slug:
        collection = get_object_or_404(Collection, slug=collection_slug)

    collections = Collection.objects.order_by('name')
    tasks = collection.task_set.order_by("description")
    
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


def createTask(request):

    slug = request.POST.get("collection")
    collection = Collection.objects.get(slug=slug)
    description = escape(request.POST.get('task-description'))
    task = Task.objects.create(description=description, collection=collection)

    context = {'task': task}
    template_name = 'tasks/partials/_task.html'
    return render(request, template_name, context)


create_task = createTask


def getTasks(request, pk):
    
    collection = get_object_or_404(Collection, pk=pk)
    tasks = collection.task_set.order_by("description")
    
    context = {"tasks": tasks}
    template_name = 'tasks/partials/tasks.html'
    return render(request, template_name, context)


get_tasks = getTasks
