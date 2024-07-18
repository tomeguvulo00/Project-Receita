from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'Receita/pages/home.html', context={
        'name': 'Tome guvulo'})


def recipe(request, id):
    return render(request,'Receita/pages/recipes.html', context={
        'name': 'Tome guvulo'})

