
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'recipes1'

urlpatterns = [
    path('',views.home, name='recipe'),
    path('recipes/category/<int:category_id>/', views.category, name='category'),
    path('recipes/<int:id>/', views.recipe, name='recipe-recipe'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)