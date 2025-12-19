import pandas as pd
import matplotlib.pyplot as plt

# Source des données : https://www.data.gouv.fr/datasets/election-presidentielle-des-10-et-24-avril-2022-resultats-definitifs-du-1er-tour/
with open("data/resultats-elections-presidentielles-2022-1er-tour.csv", encoding="utf-8") as fichier:
    contenu = pd.read_csv(fichier)
    print(contenu)

#Question 6

nb_lignes =len(contenu)
nb_colonnes= len(contenu.columns)

#Question 7

print(contenu.dtypes)

types_colonnes = {}

for colonne, dtype in contenu.dtypes.items():
    if dtype == "int64":
        types_colonnes[colonne] = "int"
    elif dtype == "float64":
        types_colonnes[colonne] = "float"
    elif dtype == "bool":
        types_colonnes[colonne] = "bool"
    else:
        types_colonnes[colonne] = "str"

for col, typ in types_colonnes.items():
    print(f"{col} : {typ}")

#Question 8 

print(contenu.head(0))

#Question 9 

inscrits = contenu["Inscrits"]
print(inscrits)

#Question 10 

sommes = []

for colonne in contenu.columns:
    sommes.append(contenu[colonne].sum())

print(sommes)


sommes_quantitatives = []

for colonne in contenu.columns:
    if types_colonnes[colonne] in ["int", "float"]:
        sommes_quantitatives.append(contenu[colonne].sum())
    else:
        sommes_quantitatives.append(None)

print(sommes_quantitatives)


#Question 11

import os

dossier_images = "diagrammes_departements"
os.makedirs(dossier_images, exist_ok=True)

for index, ligne in contenu.iterrows():
    departement = ligne["Libellé du département"]
    inscrits = ligne["Inscrits"]
    votants = ligne["Votants"]

    plt.figure()
    plt.bar(["Inscrits", "Votants"], [inscrits, votants])
    plt.title(f"Département : {departement}")
    plt.ylabel("Nombre de personnes")

    nom_fichier = departement.replace(" ", "_") \
                             .replace("/", "_") \
                             .replace("\\", "_") \
                             .replace("'", "_") + ".png"

    chemin = os.path.join(dossier_images, nom_fichier)

    plt.savefig(chemin)
    plt.close("all")


#Question 12

dossier_pie = "diagrammes_circulaires"
os.makedirs(dossier_pie, exist_ok=True)

for index, ligne in contenu.iterrows():
    departement = ligne["Libellé du département"]

    inscrits = ligne["Inscrits"]
    votants = ligne["Votants"]
    blancs = ligne["Blancs"]
    nuls = ligne["Nuls"]
    exprimes = ligne["Exprimés"]

    abstention = inscrits - votants

    valeurs = [blancs, nuls, exprimes, abstention]
    labels = ["Blancs", "Nuls", "Exprimés", "Abstention"]

    plt.figure()
    plt.pie(valeurs, labels=labels, autopct='%1.1f%%')
    plt.title(f"Département : {departement}")

    nom_fichier = departement.replace(" ", "_") \
                             .replace("/", "_") \
                             .replace("\\", "_") + "_pie.png"

    chemin = os.path.join(dossier_pie, nom_fichier)

    plt.savefig(chemin)
    plt.close()


#Question 13 

inscrits = contenu["Inscrits"]

import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
plt.hist(inscrits, bins=20, density=True, color='skyblue', edgecolor='black')
plt.title("Histogramme de la distribution des inscrits par département")
plt.xlabel("Nombre d'inscrits")
plt.ylabel("Densité")
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.savefig("histogramme_inscrits.png", dpi=300)
plt.show()

dossier_hist = "histogrammes"
os.makedirs(dossier_hist, exist_ok=True)
plt.savefig(os.path.join(dossier_hist, "histogramme_inscrits.png"), dpi=300)









