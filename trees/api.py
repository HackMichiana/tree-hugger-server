from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.authentication import Authentication, ApiKeyAuthentication, MultiAuthentication
from trees.models import Tree, Image

from django.http import HttpResponse
from tastypie.exceptions import ImmediateHttpResponse
from tastypie import http


import pdb

# class ReadAuthorization()

class CORSResource(object):
    """
    Adds CORS headers to resources that subclass this.
    """
    def create_response(self, *args, **kwargs):
        response = super(CORSResource, self).create_response(*args, **kwargs)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = 'accept, authorization, content-type'
        return response

    def method_check(self, request, allowed=None):
        if allowed is None:
            allowed = []

        request_method = request.method.lower()
        allows = ','.join(map(str.upper, allowed))

        if request_method == 'options':
            response = HttpResponse(allows)
            response['Access-Control-Allow-Origin'] = '*'
            response['Access-Control-Allow-Headers'] = 'accept, authorization, content-type'
            response['Allow'] = allows
            raise ImmediateHttpResponse(response=response)

        if not request_method in allowed:
            response = http.HttpMethodNotAllowed(allows)
            response['Allow'] = allows
            raise ImmediateHttpResponse(response=response)

        return request_method

class ImageResource(CORSResource, ModelResource):
    class Meta:
        authorization = Authorization()
        authentication = Authentication()
        allowed_methods = ['get','options']
        queryset = Image.objects.all()
        resource_name = 'image'

class TreeResource(CORSResource, ModelResource):
    images = fields.ToManyField(ImageResource, 'image_set', related_name='tree', full=True, null=True)
    class Meta:
        authorization = Authorization()
        authentication = ApiKeyAuthentication()
        allowed_methods = ['get', 'post','options']
        queryset = Tree.objects.all()
        resource_name = 'tree'
