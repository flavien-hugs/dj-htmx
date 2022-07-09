# tasks.models.py

from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Collection(models.Model):
    name = models.CharField(max_length=80)
    slug = models.SlugField(editable=False, blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.name)
        super().save(*args, **kwargs)

    @classmethod
    def get_default_collection(cls) -> "collection":
        collection, _ = cls.objects.get_or_create(name="Défaut", slug="_defaut")
        return collection

    def tasks(self):
        return Task.objects.filter(collection=self)

    def get_absolute_url(self):
        return reverse("tasks:get_tasks", kwargs={'pk': self.pk})

    def delete_collection_url(self):
        return reverse("tasks:delete_collection", kwargs={'pk': self.pk})


class Task(models.Model):
    description = models.CharField(max_length=300)
    collection = models.ForeignKey(
        to='tasks.Collection',
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.description

    def delete_task_url(self):
        return reverse("tasks:delete_task", kwargs={'pk': self.pk})
