#########   FONCTION   CALCULESALAIRE      #########

def calculeSalaire(nom_metier, nb_exp):
	if nb_exp == 4 and nom_metier == 'medecin'  : 
		salaire = 1000
	elif nb_exp == 3 and nom_metier == 'architecte' : 
		salaire = 2000
	elif nb_exp == 8 and nom_metier == 'developpeur' : 
		salaire = 3000
	return salaire


########   PRINT  #########

nom_metier = "medecin"
nb_exp = 5
salaire = calculeSalaire(nom_metier, nb_exp)
print( "salaire de " + nom_metier + " avec " + nb_exp + " experiences  : " + salaire + " euros ")

nom_metier = "architecte"
nb_exp = 3
salaire = calculeSalaire(nom_metier, nb_exp)
print( "salaire de " + nom_metier + " avec " + nb_exp + " experiences  : " + salaire + " euros ")

nom_metier = "developpeur"
nb_exp = 8
salaire = calculeSalaire(nom_metier, nb_exp)
print( "salaire de " + nom_metier + " avec " + nb_exp + " experiences  : " + salaire + " euros ")

