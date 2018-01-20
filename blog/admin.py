from django.contrib import admin
from .models import Post #tecka na zacatku ze se to importuje ze stejneho adresyre ve kterem zrovna jsme

# Register your models here.

admin.site.register(Post)
