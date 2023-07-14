from django.contrib import admin
from .models import Recipe

'''
Register/add your models here to our admin so we can interact with it in the browser.
'''
# admin.site.register(Recipe)

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'created_on')



# @admin.register(Recipe)
# class RecipeAdmin(admin.ModelAdmin):
#     list_display = ('title', 'created_on', 'prep_time', 'cook_time', 'serving_size')
#     list_filter = ('created_on', 'prep_time', 'cook_time', 'serving_size')
#     search_fields = ('title', 'description', 'instructions')
#     date_hierarchy = 'created_on'
