from django.shortcuts import render
from django.template import loader
from .models import Item
from django.http import HttpResponse

# Create your views here.
def index(request):
    item_objects = Item.objects.all()
    template = loader.get_template("food/index.html")
    context = {}
    return HttpResponse(template.render(context, request))
