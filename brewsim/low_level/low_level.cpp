#include<iostream>
#include<cpr/cpr.h>
#include<nlohmann/json.hpp>
//#include <string> 
//#include <vector>
//#include <memory>
//#include <optional>


using namespace std;

class Departement {
    int numero;
    int prix;
    int id;
  public:
	Departement(int numero, int prix): numero(numero), prix(prix) {}

	// le constructeur prenant un objet JSON et un ID
    	Departement(const nlohmann::json& json_data, int id) : numero(json_data["numero"]), prix(json_data["prix"]), id(id) {}

	/*auto afficher() const {

        std::cout << "Département \n" << numero << " Prix : " << prix << std::endl;
        
	}*/

	auto afficherR() const {
		std::cout << "Département " << numero << " Prix : " << prix << " ID : " << id << std::endl;
	}
	auto Requete() const {
	 
		//std::string url = "http://localhost:8000/departement/1";
		std::string url= "http://localhost:8000/departement/1";
		
		auto reponse = cpr::Get(cpr::Url{url});
		std::cout << "Code de réponse HTTP : " << reponse.status_code << std::endl;
		std::cout << "Contenu de la réponse : " << reponse.text << std::endl;
		
		/*
		// Parsons la réponse JSON
		if (reponse.status_code == 200) {
		    try {
		        auto json_data = nlohmann::json::parse(reponse.text);
		        // Utilisez json_data comme vous le souhaitez
		    } 
		    catch (const std::exception& e) {
		        std::cerr << "Erreur lors du parsing JSON : " << e.what() << std::endl;
		    }
		} 
		else {
		    std::cerr << "Erreur HTTP : " << reponse.status_code << std::endl;
		}*/
		
		
		 // Vérifiez si la requête a réussi (status code 200)
		if(reponse.status_code == 200) {
		    // Essayez de parser le texte JSON
		    try {
		        // Utilisez nlohmann/json pour analyser le texte JSON
		        nlohmann::json json_response = nlohmann::json::parse(reponse.text);

		        // Créez une nouvelle instance de la classe Département à partir de la réponse JSON et de l'ID
		        Departement departement_from_json(json_response, id);

		        // Affichez les informations de la nouvelle instance
		        departement_from_json.afficherR();
		    } 
		    catch (const nlohmann::json::exception& e)
		    {
		        std::cerr << "Erreur de parsing JSON : " << e.what() << std::endl;
		    }
		} 
		else 
		{
		    std::cerr << "Erreur HTTP : " << reponse.status_code << std::endl;
		}
	    }
};


/*class Machine {
    int nom;
    int prix;
  
};

class Ingredient{
std::string nom;

void afficher() const {
        std::cout << "Nom de l'ingrédient : " << nom << std::endl;

};
class QuantiteIngredient{
std::unique_ptr<Ingredient> ingredient;
int quantite;
};
class Action{
machine
char commande;
int duree;
ingredient
action parent
};
class Recette{
char nom
action
};

class Usine{
departement
char taille;
machines
recettes
stocks=
};
class Prix{
ingredient
departement
int prix;
};*/


int main(){
	
	int id = 50;

    // Création d'une instance de la classe Département avec le constructeur
    //Departement departement1(1, 1000);

    // Affichage de l'instance
    //departement1.afficher();
    
    // Effectuer une requête HTTP
   // departement1.Requete();
    
    // Création d'une instance de la classe Département avec le constructeur prenant un paramètre json data et un id
    
    nlohmann::json json_data = {{"numero", 2}, {"prix", 2000}};
    
    Departement departement_from_json(json_data, id);

    // Affichage de l'instance créée à partir de JSON
    departement_from_json.afficherR();
   
    return 0;}



