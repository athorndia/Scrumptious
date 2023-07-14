from django.db import models
# from datetime import timedelta


'''
The model allows us to save data in the database.
It describes the data that we want to have in our application.

Everytime we add a new model or make a change to a model, we need to
run a migration.

'''

# class Ingredient(models.Model):
#     amount = models.CharField(max_length=50, default='1')
#     food_item = models.CharField(max_length=200)
#     description = models.TextField()

# class Tag(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    picture = models.URLField()
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    # prep_time = models.DurationField(default=timedelta(minutes=30))
    # cook_time = models.DurationField(default=timedelta(minutes=30))
    # serving_size = models.PositiveIntegerField(default=2)
    # ingredients = models.ManyToManyField(Ingredient, related_name='recipes')
    # tags = models.ManyToManyField(Tag)
    # ratings = ***

    # def instructions(self):
#         return Instruction.objects.filter(recipe=self)

# class Instruction(models.Model):
#     recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
#     step_number = models.PositiveIntegerField()
#     step_description = models.TextField()

#     class Meta:
#         ordering = ['step_number']
