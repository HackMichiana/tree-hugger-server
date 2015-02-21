from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.authentication import Authentication
from trees.models import Tree


class TreeResource(ModelResource):
    class Meta:
        authorization = Authorization()
        authentication = Authentication()
        allowed_methods = ['get', 'post']
        queryset = Tree.objects.all()
        resource_name = 'tree'
