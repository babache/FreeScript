# Informations

Ce qui suit permet d'effectuer des cycles de charge et éviter si vous laissez brancher votre Mac d'être constament en charge.


# Equipements

Voici le minimun requis :

 * un macbook (Pro,Air) version de mac sur batterie évidement :'D
 * un plug TPLink Switch HS100, liste complete sur le [fork](https://github.com/babache/pyHS100) présent sur ton compte (Merci [GadgetReactor](https://github.com/GadgetReactor/pyHS100))

 *Le plug (lors de mon achat) était au alentour de 30€



# Installation 

Vous aurez besoin de python3, installation possible via <b>brew</b>

``` shell
$ brew install python3
 ```

Ainsi que la lib pyHS100 ([fork](https://github.com/babache/pyHS100) ou [GadgetReactor](https://github.com/GadgetReactor/pyHS100))


# Utilisation

Via la crontab toutes les 5 min je lance le script :
``` shell
$ */5 * * * * /usr/local/bin/python3 commandPlug.py
 ```

# Fonctionnement

Le script est destiné au personne qui ne possède qu'un seul plug, le script lance une recherche sur le réseau et récupère l'IP du plug.

Ensuite si il le trouve il récupère l'information de l'état (ON ou OFF) et va couper le plug si la batterie est supérieur à 95% et le coupera si la batterie est inférieur à 20%. 

A vous maintenant de définir vos niveau bas et haut ;)


