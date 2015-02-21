from django.http import JsonResponse

from .models import Tree


def upload(request, id):
    t = Tree.objects.get(id=id)
    image = t.images.create(image=request.FILES['image'])
    return JsonResponse({'status': 'lgtm', 'image_id': image.id})
