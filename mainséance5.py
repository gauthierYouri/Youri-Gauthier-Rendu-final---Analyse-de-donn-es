
#coding:utf8
import pandas as pd
import math
import scipy
import scipy.stats

# Question 1

def ouvrirUnFichier(nom):
    with open(nom, "r") as fichier:
        contenu = pd.read_csv(fichier)
    return contenu

# --- 
print("Résultat sur le calcul d'un intervalle de fluctuation")
donnees = ouvrirUnFichier("./data/Echantillonnage-100-Echantillons.csv")

# --- 
moy_p = round(donnees['Pour'].mean())
moy_c = round(donnees['Contre'].mean())
moy_s = round(donnees['Sans opinion'].mean())

# --- 3. CALCUL DES FRÉQUENCES ---
# Somme des moyennes pour obtenir le total de l'échantillon moyen
total_moyennes = moy_p + moy_c + moy_s

# Fréquences des échantillons (arrondies à 2 décimales)
f_pour = round(moy_p / total_moyennes, 2)
f_contre = round(moy_c / total_moyennes, 2)
f_sans = round(moy_s / total_moyennes, 2)

# Fréquences de la population mère (Réalité)
pop_mere_total = 2185
p_pour = round(852 / pop_mere_total, 2)
p_contre = round(911 / pop_mere_total, 2)
p_sans = round(422 / pop_mere_total, 2)

# --- 
# Taille d'un échantillon (somme des individus sur la première ligne)
n = donnees.iloc[0].sum() 
zC = 1.96

def calcul_if(p, n):
    marge = zC * math.sqrt((p * (1 - p)) / n)
    return round(p - marge, 3), round(p + marge, 3)

if_pour = calcul_if(p_pour, n)
if_contre = calcul_if(p_contre, n)
if_sans = calcul_if(p_sans, n)

# --- 
print(f"Fréquences observées : Pour={f_pour}, Contre={f_contre}, Sans={f_sans}")
print(f"Fréquences réelles   : Pour={p_pour}, Contre={p_contre}, Sans={p_sans}")
print(f"Intervalle de fluctuation (95%) pour 'Pour' : {if_pour}")

# 
print("\nRésultat sur le calcul d'un intervalle de confiance")
# ...


# Question 2

# --- 
# .iloc[0] récupère la première ligne, .tolist() la convertit en liste
ligne_echantillon = donnees.iloc[0].tolist()

# 
n_pour = ligne_echantillon[0]
n_contre = ligne_echantillon[1]
n_sans = ligne_echantillon[2]

# Calcul de l'effectif total de cet échantillon (n)
n_total_echantillon = sum(ligne_echantillon)

# Calcul des fréquences observées sur cet échantillon précis
f_p = n_pour / n_total_echantillon
f_c = n_contre / n_total_echantillon
f_s = n_sans / n_total_echantillon

# --- 
def calcul_ic(f, n):
    marge = 1.96 * math.sqrt((f * (1 - f)) / n)
    return round(f - marge, 3), round(f + marge, 3)

ic_pour = calcul_ic(f_p, n_total_echantillon)
ic_contre = calcul_ic(f_c, n_total_echantillon)
ic_sans = calcul_ic(f_s, n_total_echantillon)

# 
print(f"Échantillon 1 - Fréquence 'Pour': {round(f_p, 3)} | IC: {ic_pour}")
print(f"Échantillon 1 - Fréquence 'Contre': {round(f_c, 3)} | IC: {ic_contre}")
print(f"Échantillon 1 - Fréquence 'Sans opinion': {round(f_s, 3)} | IC: {ic_sans}")


# Question 3 

print("\nThéorie de la décision (Test de Shapiro-Wilk)")

# 1. Chargement des deux fichiers de test)
test1 = ouvrirUnFichier("./data/Loi-normale-Test-1.csv")
test2 = ouvrirUnFichier("./data/Loi-normale-Test-2.csv")

# 2. Application du test de Shapiro-Wilk
# shapiro() retourne deux valeurs : la statistique (W) et la p-value
stat1, p_val1 = scipy.stats.shapiro(test1)
stat2, p_val2 = scipy.stats.shapiro(test2)

# 3. Affichage des résultats
print(f"Fichier 1 - p-value : {p_val1:.5f}")
print(f"Fichier 2 - p-value : {p_val2:.5f}")

# 4. Conclusion logique
def interpreter_shapiro(p_value, nom_fichier):
    if p_value > 0.05:
        return f"Le {nom_fichier} suit probablement une loi normale (p > 0.05)."
    else:
        return f"Le {nom_fichier} ne suit PAS une loi normale (p < 0.05)."

print(interpreter_shapiro(p_val1, "Test 1"))
print(interpreter_shapiro(p_val2, "Test 2"))
