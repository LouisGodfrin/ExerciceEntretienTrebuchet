import math

################
##  Fonctions ##
################

def lecture_fichier(nomFichier):
    """

    Objectif : Lit un fichier et retourne son contenu sous forme de liste de listes, contenant chacune le contenu de chaque ligne du fichier.

    Paramètres : Nom d'un fichier correctement structuré

    """

    fichier = open(nomFichier, "r")

    #lecture des lignes du fichier
    ligne = fichier.readlines()
    contenu = []

    for i in ligne:
        # Utilisation de rstrip pour la suppression d'eventuels espaces en fin de ligne
        i = i.rstrip()
        # Séparation de la ligne en mots en utilisant les espaces, et ajout à la liste "contenu"
        contenu.append(i.rsplit(' '))

    # Vérification si le fichier est vide
    if contenu == []:
        print('Le fichier est vide')
        return []

    # Fermeture du fichier
    fichier.close()
    return contenu


def calibrage(contenu):
    """
    Objectif : Calcule un résultat basé sur le traitement des informations extraites des lignes du fichier, et retourne la somme de tous les calibrages extrait du fichier.

    Paramètres : contenu : Contenu du fichier mémorisé sous la forme d'une liste de liste, où chaque élément est une chaîne de caractères.

    """

    # Initialisation des variables
    resultat = 0
    TableauTemporaire = []


    # Traitement de chaque sous-liste
    for sous_liste in contenu:
        premierNombre = math.inf
        secondNombre = math.inf

        # Extraction des nombres dans la sous-liste
        for element in sous_liste:
            for char in element:
                #utilisation de isdigit() permettant de différencier s'il s'agit d'une lettre ou d'un chiffre, comme l'ensemble du contenu est de type char. 
                if(char.isdigit() and premierNombre == math.inf):
                    premierNombre = int(char)
                elif(char.isdigit() and premierNombre != math.inf):
                    secondNombre = int(char)

        # Gestion des cas où des nombres ont été trouvés
        if(premierNombre != math.inf):
            TableauTemporaire.append(premierNombre * 10)
            if(secondNombre != math.inf):
                TableauTemporaire.append(secondNombre)
            
            else:
                #Si un seul nombre dans la ligne, alors il est porté à la dizaine et on l'ajoute à lui même comme s'il était présent 2 fois.
                premierNombre = premierNombre * 10 + premierNombre
                TableauTemporaire[0] = premierNombre
                '''Ajout d'un 0 en indice 1 de TableauTemporaire pour pouvoir gérer "resulat", et le reset de TableauTemporaire, 
                   en dehors de toutes les conditions pour simplifier et aéré le code.
                '''
                TableauTemporaire.append(0) 

        # Calcul du résultat pour la sous-liste parcouru 
        resultat += TableauTemporaire[0] + TableauTemporaire[1]

        # Réinitialisation du tableau temporaire pour la prochaine itération
        TableauTemporaire = []

    return resultat
    

###########################
##  Appel des fonctions  ##
###########################

# Lecture du contenu du fichier
contenu = lecture_fichier("data.txt")

# Appel de la fonction de calibration et affichage du résultat
result = calibrage(contenu)
print(result)