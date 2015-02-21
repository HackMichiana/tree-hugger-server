from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.authentication import Authentication
from trees.models import Tree, Image


class ImageResource(ModelResource):
    class Meta:
        authorization = Authorization()
        authentication = Authentication()
        allowed_methods = ['get']
        queryset = Image.objects.all()
        resource_name = 'image'

class TreeResource(ModelResource):
    images = fields.ToManyField(ImageResource, 'image_set', related_name='tree', full=True)
    class Meta:
        authorization = Authorization()
        authentication = Authentication()
        allowed_methods = ['get', 'post']
        queryset = Tree.objects.all()
        resource_name = 'tree'
