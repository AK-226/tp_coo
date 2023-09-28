from django.db import models

# Create your models here.
class Departement(models.Model):
    numero = models.IntegerField()
    prix = models.IntegerField()

    def __str__(self):
        return f"Departement{self.numero}"

class Usine(models.Model):
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    taille = models.CharField(max_length=200)
    machines = models.IntegerField()
    recettes = models.CharField(max_length=200)
    stocks = models.IntegerField()

    def _str_(self):
        return f"Usine dans le département{self.departement.numero}"

class Ingredient(models.Model):
    nom = models.CharField(max_length= 200)

    def _str_(self):
     return f"Nom de l'ingredient{self.ingredient.nom}"

class Prix(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE,related_name="+")
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE,related_name="+")
    prix = models.IntegerField()

    def _str_(self):
        return f"Prix pour les ingrédients {self.ingredient} dans le département {self.departement.numero}"

class QuantiteIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    quantite = models.IntegerField()

    def _str_(self):
        return f"{self.quantite} {self.ingredient.nom}"

class Machine(models.Model):
    nom = models.CharField(max_length=200)

    def _str_(self):
        return self.nom

class Action(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    commande = models.CharField(max_length=200)
    duree = models.IntegerField()
    ingredients = models.CharField(Ingredients)
    action = models.CharField(max_length=200)

    def _str_(self):
        return f"Action {self.commande} sur la machine {self.machine.nom}"

class Recette(models.Model):
    nom = models.CharField(max_length=100)
    action = models.ManyToManyField('Action')

    def _str_(self):
        return self.nom
