#Question 1
def multiplication(liste):
    result = 1  
    for element in liste:
        result *= element
    return result

Liste_déchantillons = [2, 3, 6]

result = multiplication(Liste_déchantillons)

print("Résultat =", result)

#Question 2
def tri(tuple):
    return sorted(tuple, key=lambda x: x[-1])
Liste = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
result = tri(Liste)
print("Resultat =",result)

#Question 5
liste = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

liste_triee = sorted(liste, key=lambda x: float(x[1]), reverse=True)

print("Résultat attendu :", liste_triee)


#Question 6
ensemble = {0, 1, 2, 3, 4}
print("Ensemble créé :", ensemble)

print("Éléments de l'ensemble :")
for element in ensemble:
    print(element)

ensemble.add(5)
ensemble.add(6)
ensemble.add(7)
ensemble.add(8)
print("Ensemble après ajout :", ensemble)

# Supprimer des éléments
ensemble.remove(5)
ensemble.remove(7)
print("Ensemble après suppression :", ensemble)


