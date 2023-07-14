# APP LEVEL

from django.urls import path
from recipes.views import recipe_list, create_recipe, show_recipe, edit_recipe



'''
Uses the endpoints from the browser URL to fire a specific view function

This path function is used to associate a URL path expression with the function we just wrote.
Next the desired function is imported.

The urlpatterns stores path-function registrations into a list.
Inside that list, the path function says that we're going to associate
the URL path "recipes/" with the show_recipe function.

The urls.py in the recipes directory is for registering our view functions.
That's where we'll be adding more and more paths in the upcoming days.
NEEDS 3 THINGS: ***
'''


urlpatterns = [
    path("recipes/", recipe_list, name=("recipe_list")),
    path("recipes/create/", create_recipe, name="create_recipe"),
    path("recipes/<int:id>/", show_recipe, name="show_recipe"),
    path("recipes/<int:pk>/edit/", edit_recipe, name="edit_recipe"),
]
