from tastypie.resources import ModelResource
from trees.models import Tree


class TreeResource(ModelResource):
    class Meta:
        queryset = Tree.objects.all()
        resource_name = 'tree'
