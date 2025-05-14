from django.shortcuts import render

# Create your views here.
from flower.models import Flower
from django.shortcuts import get_object_or_404  
def flower(request):
    q = request.GET.get('q', None)
    flower = ''
    if q is None or q is "":
        flower = Flower.objects.all()
    elif q is not None:
        flower = Flower.objects.filter(title__contains=q)
    return render(request, 'flower/flower.html', {'flower': flower })
def detail(request, slug=None):
    flower = get_object_or_404(Flower, slug=slug)
    return render(request, 'flower/detail.html', locals())
