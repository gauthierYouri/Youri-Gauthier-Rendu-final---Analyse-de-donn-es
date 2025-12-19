
#coding:utf8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Source des données : https://www.data.gouv.fr/datasets/election-presidentielle-des-10-et-24-avril-2022-resultats-definitifs-du-1er-tour/

df = pd.read_csv("data/resultats-elections-presidentielles-2022-1er-tour.csv", encoding="utf-8")
print(df.head())

#Question 5 : 

quant_cols = ["Inscrits","Abstentions","Votants","Blancs","Nuls","Exprimés","Voix"]
quant_df = df[quant_cols]

results = {}
for col in quant_cols:
    series = quant_df[col].dropna()
    results[col] = {
        "Moyenne": round(series.mean(), 2),
        "Médiane": round(series.median(), 2),
        "Mode": round(series.mode().iloc[0], 2) if not series.mode().empty else np.nan,
        "Écart type": round(series.std(), 2),
        "Écart absolu à la moyenne": round((abs(series - series.mean())).mean(), 2),
        "Étendue": round(series.max() - series.min(), 2),
        "Distance interquartile": round(series.quantile(0.75) - series.quantile(0.25), 2),
        "Distance interdécile": round(series.quantile(0.9) - series.quantile(0.1), 2)
    }

#Question 6
for col, stats in results.items():
    print(f"\nParamètres pour {col}:")
    for k, v in stats.items():
        print(f"  {k}: {v}")

#Question 7 

plt.figure(figsize=(12,8))
quant_df.boxplot()
plt.title("Boîtes de dispersion des colonnes quantitatives")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("boites_dispersion.png")  # Sauvegarde l'image
plt.show()

#Question 8 

results_df = pd.DataFrame(results).T
results_df.to_csv("parametres_elections.csv", index=True)
results_df.to_excel("parametres_elections.xlsx", index=True)


#Question 9

with open("data/island-index.csv", encoding="utf-8") as f:
    contenu = pd.read_csv(f)

print(pd.DataFrame(contenu))
df=pd.DataFrame(contenu)



#Question 10

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("data/island-index.csv", encoding="latin1")


liste_surface = []
for surface in df["Surface (km2)"]:
    if surface <= 10:
        categorie = "]0, 10]"
    elif 10 < surface <= 25:
        categorie = "]10, 25]"
    elif 25 < surface <= 50:
        categorie = "]25, 50]"
    elif 50 < surface <= 100:
        categorie = "]50, 100]"
    elif 100 < surface <= 2500:
        categorie = "]100, 2500]"
    elif 2500 < surface <= 5000:
        categorie = "]2500, 5000]"
    elif 5000 < surface <= 10000:
        categorie = "]5000, 10000]"
    else:
        categorie = ">= 10000"
    liste_surface.append(categorie)


df["Classe_Surface"] = liste_surface
liste_comptage = df["Classe_Surface"].value_counts()


print("Nombre d'îles par catégorie :")
print(liste_comptage)


plt.figure(figsize=(10, 6))
liste_comptage.plot(kind='bar', color='skyblue')
plt.title("Répartition des îles par surface")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()