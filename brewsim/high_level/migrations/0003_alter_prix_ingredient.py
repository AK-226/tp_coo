# Generated by Django 4.2.5 on 2023-10-04 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("high_level", "0002_machine_prix"),
    ]

    operations = [
        migrations.AlterField(
            model_name="prix",
            name="ingredient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="high_level.ingredient"
            ),
        ),
    ]
