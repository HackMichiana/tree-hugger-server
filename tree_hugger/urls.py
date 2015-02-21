from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from django.shortcuts import render
from tastypie.api import Api

import trees.api as treesapi
from trees import views

api = Api(api_name='v1')
api.register(treesapi.TreeResource())

urlpatterns = [
    # Examples:
    # url(r'^$', 'tree_hugger.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(api.urls)),
    url(r'^upload/', views.upload),
    url(r'^$', render, {'template_name': 'map.html'}),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
