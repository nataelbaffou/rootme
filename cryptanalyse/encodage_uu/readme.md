# Encodage - ASCII

Challenge: https://www.root-me.org/fr/Challenges/Cryptanalyse/Encodage-UU


## Resources

PDF, explication des différents encodings permettant une conversion de binaire à plein text.
[EN - Encodings format.pdf](resources/EN%20-%20Encodings%20format.pdf)

## Fonctionnement
Le format uuencoding est un ancien format provenant des systèmes unix. 
Ils ne sont quasiment plus utilisés car les extensions MIME, sont désormais généralement utilisé. Le format base64 est celui qui remplace majoritairmeent uuencoding.

Un text encodé par uuencoding contient
```
begin [mode] [filename]
[données encodées, potentiellement sur plusieurs lignes]
[1 ligne vide encodée]
end
```

Le `mode` correspond à la valeur octale des droits d'accès sur linux, comme pour `chmod` par exemple
`filename` correspond au nom de fichier (sans information de dossier)

Pour encoder on va utiliser 3 octets et les transformer en 4 octets imprimables.
Pour celà on va répartir les 24 (8*3) bits en 4 paquets de 6 bits.
Cette méthode est la même pour uuencoding, xxencoding ou encore base 64.

Par la suite on va utiliser une table de conversion pour traduire les 6 bits vers l'octet que l'on souhaite afficher.
Pour décoder on fait l'inverse, on convertit l'octet en 6 bits et on reconstruit les données de départ en réagencant les bits pour former les données.

Pour uuencoding on utilise tous les caractères ascii dans l'ordre à partir de l'espace " " (valeur 32). 
Cependant l'espace n'est pas vraiment un caractère imprimable, il est donc remplacé par un back tick "`"

On ajoute également un unique caractère en début de chaque ligne qui indique le nombre d'octet de données à décoder.
Ainsi pour 22 octets de données, on va avoir pour premier caractère `6` suivi de 22/3=7,3 => 8*4=32 octets des données encodées dont deux octets nuls à la fin.

## Résolution
En python le module `uu` pour encoder et décoder est déprécié depuis la version 3.11 et supprimé depuis la version 3.13.
J'ai donc uniquement réalisé la conversion manuellement mais elle pourrait aussi bien être faite avec une version de python antérieure.
Une subtilité du langage python est qu'on ne peut pas définir un nombre uniquement sur 8 bits, ainsi un décalage de bits vers la gauche ne fait que multiplier par deux mais on ne va pas perdre les bits de poids fort.
J'ai donc été obligé de réaliser en plus un ET binaire afin de garder mes opérations sur 8 bits.
Pour réaliser mes operations, je n'ai pas réalisé de vérifications sur les données, j'ai donc pris les lignes entre les lignes "begin" et "end".
Je n'ai pas tenu compte du nombre d'octets à récupérer et donc ignoré le premier caractère de chaque ligne.
Ensuite pour chaque groupe de 4 octets je regénère les 3 octets d'origines en faisant les décalages de bits nécessaires.

En Rust j'ai utilisé la même méthode, mais je n'ai pas eu de problème à utiliser les octets en u8. pour la conversion backtick/espace, j'ai utilisé cette fois-ci le modulo pour éviter d'avoir à faire une opération supplémentaire sur les chaînes des caractères.