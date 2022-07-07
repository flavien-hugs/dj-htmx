from django.contrib import admin

from tasks.models import Collection, Task


admin.site.register(Task)
admin.site.register(Collection)
