# tasks.views.py

from django.shortcuts import render
from django.http import HttpResponse


def homePageView(request):
    template_name = 'tasks/_list.html'
    context = {}
    return render(request, template_name, context)


index_view = homePageView


def createCollectionView(request):
    return HttpResponse("")


create_collection = createCollectionView
