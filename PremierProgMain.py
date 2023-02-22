#Première fonction
def groupe1(l):
    for i in range(len(l)):
        # Mettre les mots de la liste en minuscule en commençant par une lettre majuscule et enlever les espaces avant et arrière.
        l[i] = l[i].strip().capitalize()

    # Traiter les verbes selon leurs terminaison pour les mettre à l'infinitif.
    #Je parcours la liste dans l'ordre inverse pouvoir supprimer les intrus sans affecter l'ordre de traitement de ma liste
    for i in range(len(l)-1, -1, -1):
        if l[i].endswith("ees"):
            l[i] = l[i][:-2]+"r"
        elif l[i].endswith("e"):
            l[i] = l[i]+"r"
        elif l[i].endswith(("es", "ez")):
            l[i] = l[i][:-1]+"r"
        elif l[i].endswith(("ent","ons")):
            l[i] = l[i][:-3] + "er"
        #Suppression des intrus.
        else:
            l.pop(i)
    #Suppression des doublons
    l = list(set(l))

    #Tri de la liste
    l.sort()
    return l



#Fonction exigée par la professeur
def mme(l):
    for i in range(len(l)):
        l[i] = l[i].lower().strip();
        if l[i].endswith("e"):
            l[i] = l[i] + "r"
        elif l[i].endswith(("es", "ez")):
            l[i] = l[i][:-1] + "r"
        elif l[i].endswith("ons"):
            l[i] = l[i][:-3] + "er"
        elif l[i].endswith("ent"):
            l[i] = l[i][:-2] + "r"
    #Je parcours la liste pour supprimer les intrus.
    for i in reversed(l):
        if i.endswith("er") == False or i.endswith("eer") == True:
            del (i);
        l = list(set(l));
        l.sort()
    return l


#Je teste mes fonctions

#Dictionnaire de verbes à tester
verbes =["amenons","OUBLIENT","bash","Commencons","achetez" ,"Achete", "raconte", "oubliez","TESTENT","oublient","Testez","racontes","oubliez","AMene","AMENENT","racontons","testons","ACHETENT","RACONTEZ","Amenees","OUBLI","achetons","Oublient","COMMENCES","Oubliez","RACONTEZ","parle","amenes","OUBLIONS"];

#Jeu utilisé par la première fonction
test1=verbes

#Jeu utilisé par la deuxième fonction
test2=verbes


print("Début de la fonction personnelle.\n")
test1=groupe1(test1);
for i in range (len(test1)):
    print (test1[i]);
print("\n")


print("Début de la fonction exigée par la prof.\n")
test2=mme(test2);
for i in (test2):
    print (i)
print("\n")


