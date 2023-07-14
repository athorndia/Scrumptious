# Generated by Django 4.2.3 on 2023-07-12 23:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_rename_instructions_recipe_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='cook_time',
            field=models.DurationField(default=datetime.timedelta(seconds=1800)),
        ),
        migrations.AddField(
            model_name='recipe',
            name='instructions',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='recipe',
            name='prep_time',
            field=models.DurationField(default=datetime.timedelta(seconds=1800)),
        ),
        migrations.AddField(
            model_name='recipe',
            name='serving_size',
            field=models.PositiveIntegerField(default=2),
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(to='recipes.ingredient'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(to='recipes.tag'),
        ),
    ]