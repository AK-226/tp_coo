from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Departement)
admin.site.register(models.Usine)
admin.site.register(models.Prix)
admin.site.register(models.Ingredient)
