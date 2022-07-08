# tasks.views.py

from django.http import HttpResponse
from django.utils.html import escape
from django.template.loader import render_to_string
from django.shortcuts import render, redirect, get_object_or_404

from tasks.models import Collection, Task


def homePageView(request):

    context = {}

    collection_slug = request.GET.get("collection")
    collection = Collection.get_default_collection()

    if collection_slug:
        collection = get_object_or_404(Collection, slug=collection_slug)

    collections = Collection.objects.order_by('name')
    context['collections'] = render_to_string(
        'tasks/partials/_collection.html', context={"collections": collections}
    )

    tasks = collection.task_set.order_by("description")
    context['tasks'] = render_to_string(
        'tasks/partials/_task.html', context={"tasks": tasks}
    )
    
    template_name = 'tasks/_list.html'
    return render(request, template_name, context=context)


index_view = homePageView


def createCollectionView(request):

    collection_name = escape(request.POST.get('collection-name'))
    collection, created = Collection.objects.get_or_create(name=collection_name)
    
    if not created:
        return HttpResponse("Cette collection existe déjà !", status=409)
    
    return HttpResponse(f"<h2>{collection.name}</h2>")


create_collection = createCollectionView


def createTask(request):

    collection = Collection.get_default_collection()
    description = escape(request.POST.get('task-description'))
    Task.objects.create(description=description, collection=collection)
    
    return HttpResponse(description)


create_task = createTask


def getTasks(request, pk):
    
    collection = get_object_or_404(Collection, pk=pk)
    tasks = collection.task_set.order_by("description")
    task = [task.description for task in tasks]
    return HttpResponse("<br>".join(task))


get_tasks = getTasks
