
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='receitas.ao'),
    path('recipes/<int:id>/', views.recipe, name='recipe-recipe'),
]

