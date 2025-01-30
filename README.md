# OAFD_TP2
rendu du TP2 pour le cours de Optimisation Avancée pour la Fouille de Données, FloatPair

**Objectif**

L’objectif de ce TP est d’implémenter le problème FloatPairs et d’utiliser l’algorithme de recherche locale et de recherche génétique sur ce problème en modifiant les paramètres de ces algorithmes afin d’analyser les résultats afin de comprendre l’influence des différents paramètres sur la convergence des algorithmes.

Le problème FloatPairs est un problème d’optimisation jouet cherchant à maximiser le comptage des paires de flottants de signes différents dans une séquence de flottant donnée. 

Une paire de flottant est définie comme deux flottants de signes différents, par exemple -5.0 et 3.0, ou 6.0 et -2.5.

La solution [-10.00, 5.00, 6.25, 3.14, -8.7, -9.75, 1.36,-9.99] comporte les paires suivantes : 

-  -10.00 et 5.00 (positions 1 et 2)

-  3.14 et -8.7 (positions 4 et 5) 

-  9.75 et 1.36 (positions 6 et 7) 

- 1.36 et -9.99 (positions 7 et 8) 

Il y a donc un total de 4 paires de signes différent adjacentes dans la séquence donnée et donc le score sera de 4. 
