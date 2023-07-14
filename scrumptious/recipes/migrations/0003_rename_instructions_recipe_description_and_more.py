# Generated by Django 4.2.3 on 2023-07-12 21:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_recipe_delete_recipes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='instructions',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='ingredients',
        ),
        migrations.AddField(
            model_name='recipe',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='picture',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]