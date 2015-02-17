from django.contrib import admin
from trees.models import Tree

# Register your models here.
class TreeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tree, TreeAdmin)
