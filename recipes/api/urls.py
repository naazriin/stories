from django.urls import path
from recipes.api.views import categories, tags, recipes, recipes_update, RecipeListCreateApiView, RecipeRetrieveUpdateView

urlpatterns = [
    path('cats/', categories, name='categories'),
    path('tags/', tags, name='tags'),
    # path('recipes/', recipes, name='recipes'),
    path('recipes/', RecipeListCreateApiView.as_view(), name='recipes'),

    # path('recipes/<int:pk>', recipes_update, name='recipes_update')
    path('recipes/<int:pk>', RecipeRetrieveUpdateView.as_view(), name='recipes_update')
 
]