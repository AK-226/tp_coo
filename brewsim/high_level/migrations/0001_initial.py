# Generated by Django 4.2.5 on 2023-09-27 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Departement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("numero", models.IntegerField()),
                ("prix", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Ingredient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Usine",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("taille", models.CharField(max_length=200)),
                ("machines", models.IntegerField()),
                ("recettes", models.CharField(max_length=200)),
                ("stocks", models.IntegerField()),
                (
                    "departement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="high_level.departement",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Prix",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ingredient", models.CharField(max_length=200)),
                ("prix", models.IntegerField()),
                (
                    "departement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="high_level.departement",
                    ),
                ),
            ],
        ),
    ]