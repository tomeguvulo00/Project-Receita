from django.contrib import admin
from .models import Category, ReceitasAo


class CategoryAdmin(admin.ModelAdmin):

  
    ...
@admin.register(ReceitasAo)
class RecipeAdmin(admin.ModelAdmin):
    
 
  ...

admin.site.register(Category, CategoryAdmin)

