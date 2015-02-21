from django.contrib import admin
from trees.models import Tree, Image


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0

class TreeAdmin(admin.ModelAdmin):
    list_display = ('id', 'condition', 'height', 'diameter')
    inlines = [ImageInline]

admin.site.register(Tree, TreeAdmin)
