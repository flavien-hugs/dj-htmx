# tasks.views.py

from django.http import HttpResponse
from django.utils.html import escape
from django.shortcuts import render, redirect

from tasks.models import Collection, Task


def homePageView(request):

    collections = Collection.objects.order_by('name')
    template_name = 'tasks/_list.html'
    context = {'collections': collections}

    return render(request, template_name, context)


index_view = homePageView


def createCollectionView(request):

    collection_name = escape(request.POST.get('collection-name'))
    collection, created = Collection.objects.get_or_create(name=collection_name)
    if not created:
        return HttpResponse("Cette collection existe déjà !", status=409)
    return HttpResponse(f"<h2>{collection.name}</h2>")


create_collection = createCollectionView
