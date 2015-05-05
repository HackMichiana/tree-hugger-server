from django.http import JsonResponse

from django.views.generic import CreateView

from .models import Tree
from .forms import TreeForm

try:
    import ipdb as pdb
except:
    import pdb


def upload(request, id):
    t = Tree.objects.get(id=id)
    image = t.images.create(image=request.FILES['image'])
    return JsonResponse({'status': 'lgtm', 'image_id': image.id})

class AddATree(CreateView):
    form_class = TreeForm
    template_name = 'add-a-tree.html'
    success_url = '/'

    def get_form(self, *args, **kwargs):
        res = super(AddATree, self).get_form(*args, **kwargs)
        pdb.set_trace()
        return res;
