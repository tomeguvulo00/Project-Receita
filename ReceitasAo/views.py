from django.shortcuts import render
from utils.recipes.factory import make_recipe
from ReceitasAo.models import ReceitasAo
# Create your views here.

def home(request):
    recipes = ReceitasAo.objects.all().order_by('-id')
    return render(request,'recipes/pages/home.html', context={
        'recipes': recipes,
        })

def category(request, category_id):
    recipes = ReceitasAo.objects.filter(category__id=category_id).order_by('-id')
    return render(request,'recipes/pages/home.html', context={
        'recipes': recipes,
        })

def recipe(request, id):
    return render(request,'recipes/pages/recipes.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
        })



