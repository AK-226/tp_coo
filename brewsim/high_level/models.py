from django.db import models

# Create your models here.
class Departement(models.Model):
    numero = models.IntegerField()
    prix = models.IntegerField()

    def __str__(self):
        return f"Departement{self.numero}"

class Machine(models.Model):
    nom = models.CharField(max_length=200)
    prix =models.IntegerField()

    def __str__(self):
        return self.nom
class Ingredient(models.Model):
    nom = models.CharField(max_length=200)

    def __str__(self):
     return self.nom

class QuantiteIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantite = models.IntegerField()

    def __str__(self):
        return f"{self.quantite} {self.ingredient.nom}"

class Action(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    commande = models.CharField(max_length=200)
    duree = models.IntegerField()
    ingredient = models.ManyToManyField(QuantiteIngredient)
    action_parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True, related_name="actions_children")

    def __str__(self):
        return f"Action {self.commande} sur la machine {self.machine.nom}"

class Recette(models.Model):
    nom = models.CharField(max_length=200)
    action = models.ForeignKey(Action, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Usine(models.Model):
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    taille = models.CharField(max_length=200)
    machines = models.ManyToManyField(Machine)
    recettes = models.ManyToManyField(Recette)
    stocks = models.ManyToManyField(QuantiteIngredient)

    def __str__(self):
        return f"Usine dans le département{self.departement.numero}"


class Prix(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE,related_name="+")
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE,related_name="+")
    prix = models.IntegerField()

    def __str__(self):
        return f"Prix pour les ingrédients {self.ingredient} dans le département {self.departement.numero}"
