# Encodage - ASCII

Challenge: https://www.root-me.org/fr/Challenges/Cryptanalyse/Encodage-ASCII


## Resources

Image de la table ASCII
![EN - ASCII Table.gif](resources/EN%20-%20ASCII%20Table.gif)

## Résolution
En ouvrant le fichier texte donné par l'énoncé on se rend compte que le texte est probablement est hexadécimale.
Je suppose donc qu'il faut donc regrouper les caractères deux par deux et les convertir selon le tableau de la table ascii.

En python c'est simple. Il existe un module intégré "bytearray" qui permet de tout faire en une seule commande.

En Rust j'ai décidé de lire chaque paire de caractères, récupérer la valeur décimale puis de récupèrer la caractère correpondant en changeant le type.
Je parse directement le l'array &str, ce qui fonctionne dans ce cas car tous les caractères sont en ascii (donc chacun 1 byte).
