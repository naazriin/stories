from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Category, Reciepes, Favorites
from django.views.generic import ListView, DetailView


class RecipeListView(ListView):
    model = Reciepes
    template_name = 'recipes.html'
    context_object_name = 'recipes'
    paginate_by = 4

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
    

def recipes(request):
    recipes = Reciepes.objects.all()

    
    # sessions = request.COOKIES.get('favs', [])

    if request.user.is_authenticated:
        user = request.user
        user_favs = [i.recipe for i in user.favorites.all()]
        for i in recipes:
            if i in user_favs:
                i.is_fav = True
            else:
                i.is_fav = False
    else:
        sessions = request.session.get('favs', [])
        if sessions:
            print(sessions, '----------------')
            for i in recipes:
                if i.id in sessions:
                    i.is_fav = True
                else:
                    i.is_fav = False

    context = {
        'recipes': recipes,
        # 'categories': categories
    }
    return render(request, 'recipes.html', context)



class RecipeDetailView(DetailView):
    template_name = 'single.html'
    model = Reciepes
    context_object_name = 'recipes'


def recipe_single(request, slug):
    # recipe = Reciepes.objects.get(id = recipe_id)
    recipe = Reciepes.objects.get(slug = slug)

    context = {
        'recipes': recipe
    }

    return render(request, 'single.html', context)



def add_to_fav(request, id):
    recipe = Reciepes.objects.get(id = id)
    # recipe = get_object_or_404(Reciepes, id=id)
    user = request.user
    if user.is_authenticated:
        if Favorites.objects.filter(user=user, recipe=recipe).first() == None:
            Favorites.objects.create(user=user, recipe=recipe)
            messages.add_message(request, messages.SUCCESS, 'Recipe added to favorites')
        else:
            messages.add_message(request, messages.INFO, 'Recipe already in favorites')
    else:

        if recipe:
            sessions = request.session.get('favs', [])
            # sessions = request.COOKIES.get('favs', [])

            print(sessions, '--------------------------------')
            if not (recipe.id in sessions):
                request.session['favs'] = sessions
                # request.COOKIES['favs'] = sessions
                # request.set_cookie('favs', sessions)
                sessions.append(recipe.id)
                messages.add_message(request, messages.SUCCESS, 'Recipe added to favorites')
            else:
                messages.add_message(request, messages.INFO, 'Recipe already in favorites')
    return redirect('recipes')


def remove_from_fav(request, id):
    recipe = get_object_or_404(Reciepes, id=id)
    if request.user.is_authenticated:
        user = request.user
        fav = Favorites.objects.filter(user=user, recipe=recipe).first()
        if fav:
            fav.delete()
            messages.add_message(request, messages.SUCCESS, 'Recipe removed from favorites')
        else:
            messages.add_message(request, messages.INFO, 'Recipe not in favorites')
    else:
        sessions = request.session.get('favs', [])
        # sessions = request.COOKIES.get('favs', [])
        if recipe:
            if recipe.id in sessions:
                sessions.remove(recipe.id)
                request.session['favs'] = sessions
                request.COOKIES['favs'] = sessions
                messages.add_message(request, messages.SUCCESS, 'Recipe removed from favorites')
            else:
                messages.add_message(request, messages.INFO, 'Recipe not in favorites')


    return redirect('recipes')