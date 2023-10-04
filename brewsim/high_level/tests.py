from django.test import TestCase

# Create your tests here.
from .models import machine
from .models import departement
from .models import ingredient
from .models import quantiteIngredient
from .models import prix

Class MachineModelTests(TestCase):
def test_usine_creation(self):
    self.assertEqual(Machine.objects.count(), 0)
    Machine.objects.create(nom="fermenteur", prix=1_000)
    self.asssertEqual(Machine.objects.count(), 1)

Class CostsModelTests(TestCase):
def test_costs(self):

    Machine.objects.create(nom="fermenteur", prix=1_000)
    Machine.objects.create(nom="brasseur", prix=2_000)

    departements= Departement.objects.create(numero=31, prix=2_000)


    houblon = Ingredient.objects.create(nom="houblon")

    orge = Ingredient.objects.create(nom="orge")

    QuantiteIngredient.objects.create(ingredient=houblon,quantite=50)

    QuantiteIngredient.objects.create(ingredient=orge,quantite=100)

    Prix.objects.create(ingredient=houblon,departement=departements,prix=20)

    Prix.objects.create(ingredient=orge,departement=departements,prix=10)

    usine = Usine.objects.create(departement=departements, taille='50', machines=2, recettes='...', stocks=50)

    result = usine.costs()
    print(result)

#------------------------------

# Créez un département
#departement = Departement.objects.create(numero=31, prix=2000)

# Créez une usine avec les caractéristiques du scénario de test
#usine = Usine.objects.create(departement=departement, taille='50', machines=2, recettes='...', stocks=50)

# Assurez-vous que les ingrédients nécessaires existent avec les bons prix
#Ingredient.objects.create(nom='houblon')
#Ingredient.objects.create(nom='orge')
#Prix.objects.create(ingredient=Ingredient.objects.get(nom='houblon'), departement=departement, prix=20)
#Prix.objects.create(ingredient=Ingredient.objects.get(nom='orge'), departement=departement, prix=10)

# Créez des machines avec les coûts spécifiés
#Machine.objects.create(nom='Machine1', prix=1000)
#Machine.objects.create(nom='Machine2', prix=2000)

# Appelez la méthode costs() et vérifiez le résultat
#result = usine.costs()
#print(result)  # Devrait afficher 105000€
