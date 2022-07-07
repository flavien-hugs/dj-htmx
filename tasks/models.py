# tasks.models.py

from django.db import models


class Collection(models.Model):
    name = models.CharField(max_length=80)
    slug = models.SlugField(editable=False)

    def __str__(self) -> str:
        return self.name

    @classmethod
    def get_default_collection(cls) -> "collection":
        collection, _ = cls.objects.get_or_create(name="Défaut", slug="_defaut")
        return collection


class Task(models.Model):
    description = models.CharField(max_length=300)
    collection = models.ForeignKey(
        to='tasks.Collection',
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.collection
