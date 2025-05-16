Air Quality Index (AQI) Prediction in India


**1.	Objectif de la Webapp**

Pourqoui ?

La pollution de l’air est un enjeu majeur de santé publique. L’Indice de Qualité de l'Air (AQI) est un indicateur standardisé utilisé pour communiquer le niveau de pollution atmosphérique et ses effets potentiels sur la santé.

Objectif

L'objectif de cette webapp est de prédire l'Indice de Qualité de l'Air (AQI) en Inde en fonction des niveaux de différents polluants. Elle permet aux utilisateurs d'entrer les valeurs moyennes de polluants pour estimer la qualité de l'air selon la norme nationale indienne AQI.


**2.	Choix du Dataset**

Pour ce projet, nous avons utilisé le dataset "India Air Quality Index (2024)" disponible sur Kaggle. Ce dataset offre une vue d'ensemble complète de la qualité de l'air dans diverses villes et régions de l'Inde. Il a été choisi pour plusieurs raisons:

•	Pertinence : Il inclut des mesures de polluants clés tels que PM2.5, PM10, NO2, SO2, CO, et O3, qui sont essentiels pour le calcul de l'AQI.

•	Représentativité : Les données couvrent différentes villes et régions de l'Inde, permettant des comparaisons régionales et une analyse approfondie.

•	Accessibilité : Le dataset est facilement accessible et téléchargeable depuis Kaggle, ce qui facilite son utilisation pour des projets de machine learning.

Aperçu du Dataset

Pour un aperçu détaillé du dataset et des composants clés, veuillez consulter la page du dataset sur Kaggle : https://www.kaggle.com/datasets/bhadramohit/india-air-quality-index2024-dataset 

En utilisant ce dataset, nous nous assurons que notre modèle est entraîné sur des données réelles et pertinentes, ce qui améliore la fiabilité des prédictions de l'AQI.



**3.	Choix du Modèle**

Pour ce projet, nous avons testé deux modèles de régression afin de déterminer lequel était le plus adapté pour prédire l'Indice de Qualité de l'Air (AQI) : le modèle RandomForestRegressor et le modèle de Régression Linéaire. Chaque modèle prend en entrée les niveaux des différents polluants et produit une prédiction de l'AQI.
Voici les résultats de l'évaluation de ces deux modèles :

**Évaluation des Modèles**

Modèle RandomForestRegressor

•	Performance sur la base d'apprentissage :  
•	RMSE (train) : 2.9956  
•	R² (train) : 0.9991  
•	Performance sur la base de test :  
•	RMSE (test) : 14.6440  
•	R² (test) : 0.9759  

Modèle de Régression Linéaire

•	Performance sur la base d'apprentissage :  
•	RMSE (train) : 12.5034  
•	R² (train) : 0.9841  
•	Performance sur la base de test :  
•	RMSE (test) : 13.5718  
•	R² (test) : 0.9793  
 	
**Sélection du Modèle**

Sur la base des résultats obtenus, nous avons choisi le modèle de Régression Linéaire pour notre application. Bien que le modèle RandomForestRegressor ait montré une performance légèrement meilleure sur les données d'apprentissage, le modèle de Régression Linéaire a démontré une meilleure généralisation sur les données de test, avec un RMSE et un R² comparables, voire légèrement meilleurs. Cela indique une meilleure capacité à prédire de nouvelles données non vues, ce qui est crucial pour une application de prédiction en temps réel.
 	
**Analyse des Résultats**

Une fois le modèle de Régression Linéaire sélectionné, nous avons analysé les coefficients du modèle pour comprendre l'impact de chaque polluant sur l'Indice de Qualité de l'Air (AQI). Voici comment nous avons procédé :

•	Extraction des Coefficients : Les coefficients pour chaque polluant (PM2.5, PM10, NO2, NH3, SO2, CO, et O3) ont été extraits.
•	Interprétation des Coefficients:

Les coefficients permettent de déterminer l'impact relatif de chaque polluant sur l'AQI.
-	Un coefficient positif indique une détérioration de la qualité de l'air avec l'augmentation du polluant.
-	Un coefficient négatif indique une amélioration de la qualité de l'air avec l'augmentation du polluant.

•	Résultats de l'Analyse :  
-	Intercept : 11.1898  
-	Coefficients :  
•	PM2.5 : 0.751033  
•	PM10 : 0.267372  
•	NO2 : 0.046121  
•	NH3 : -0.000651  
•	SO2 : 0.064195  
•	CO : -0.002072  
•	OZONE : -0.035897  

•	Interprétation :  
-	PM2.5 et PM10 ont les impacts les plus significatifs sur la détérioration de la qualité de l'air.  
-	NO2 et SO2 ont un impact positif mais moindre.  
-	NH3, CO, et OZONE ont des effets minimes ou légèrement positifs sur la qualité de l'air.  

*Cette analyse aide à identifier les polluants les plus influents pour cibler les efforts de réduction de la pollution.*

**Amélioration du modèle**

Pour améliorer le modèle de régression linéaire, nous avons exploré la réduction des variables en supprimant celles avec des coefficients proches de zéro (NH3_Avg, CO_Avg, OZONE_Avg) pour le rendre plus interprétable et plus rapide.

Résultats du Modèle Réduit  

•	Performance sur la base d'apprentissage :  
•	RMSE (train) : 12.7186  
•	R² (train) : 0.9830  
•	Performance sur la base de test :  
•	RMSE (test) : 14.6438  
•	R² (test) : 0.9779  
Comparaison avec le Modèle Complet

Le modèle complet a de meilleures performances avec une différence d'environ 1 point de RMSE et 0.001 de R². Bien que le modèle réduit soit presque aussi performant, plus simple et plus rapide, nous avons décidé de garder le modèle complet pour sa performance plus stable et légèrement meilleure sur les données de test.


**4.	Fonctionnement Global de l'Application**


a.  Entrée des Niveaux de Polluants : Les utilisateurs entrent les valeurs moyennes des différents polluants (PM2.5, PM10, NO2, NH3, SO2, CO, et O3).  

b.	Prédiction de l'AQI : En cliquant sur le bouton "Predict AQI", l'application utilise le modèle de régression pour prédire l'AQI basé sur les niveaux de polluants entrés.  

c.	Affichage des Résultats : L'application affiche le résultat de la prédiction de l'AQI, ainsi qu'une interprétation de la qualité de l'air (par exemple, "Acceptable air quality, but sensitive individuals may feel mild effects").  


***Technologies Utilisées***

•	Interface Utilisateur : Streamlit  

•	Backend : Python  

•	Modèle de Machine Learning : Modèle de régression (utilisant scikit-learn)  


***Instructions d'Installation et d'Utilisation***

1.	Clonez le dépôt de l'application depuis GitHub: 
    https://github.com/inessd91/prediction_python.git

2.	Installez les dépendances nécessaires en utilisant pip install  
3.  Exécutez le fichier Jupyter Notebook (Dataset.ipynb) pour créer le modèle  
4.	Lancez l'application en exécutant le fichier principal avec Streamlit : streamlit run app.py  
5.	Ouvrez votre navigateur et accédez à l'URL fournie par Streamlit pour utiliser l'application : Par défaut, Streamlit ouvrira automatiquement une nouvelle fenêtre de navigateur avec l'application. Si ce n'est pas le cas, vous pouvez accéder à l'application en suivant l'URL affichée dans le terminal  

***Exemple d'Utilisation***

1.	Entrez les valeurs des polluants dans les champs correspondants.  
2.	Cliquez sur le bouton "Predict AQI".  
3.	Visualisez le résultat de la prédiction de l'AQI et l'interprétation de la qualité de l'air.  




