from django.shortcuts import render, get_object_or_404, redirect
from recipes.models import Recipe
from recipes.forms import RecipeForm

'''
Views take requests from browser, interpret the request and
retrieve any necessary data from your database and render the
requested template.

That render function always takes the request object as its first argument.
The second argument is the path to our HTML file that Django will send back to the browser.

Djanjo Pattern: Gets the data -> puts data in a data structure -> render the HTML with that data
'''

#########################################################################################################
# Veiw Function: Gets the data -> puts data in a context dictionary -> renders the HTML with that context data
def show_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    context = {
        "recipe_object": recipe,
    }
    return render(request, 'recipes/detail.html', context) # Automatically looks in template folder

def recipe_list(request):
    recipes = Recipe.objects.all()
    context = {
        "recipe_list": recipes,
    }
    return render(request, 'recipes/list.html', context)

#########################################################################################################
def create_recipe(request):
    if request.method == "POST":
        # We should use the form to validate the values and save them to the database
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            # If all goes well, we can direct the browser to another page and leave the function
            return redirect("recipe_list")
    else:
        # Create an instance of the django model form class
        form = RecipeForm()
        # Put the form in the context
        context = {
            "form": form,
        }
    # Render the HTML template with the form
    return render(request, "recipes/create.html", context)

#########################################################################################################
def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect("recipe_list")
    else:
        form = RecipeForm(instance=recipe)

    context = {
      "recipe": recipe,
      "form": form,
    }
    return render(request, "recipes/edit.html", context)

#########################################################################################################
