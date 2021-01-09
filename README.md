# Autopadlet
On peut trouver ici le code source du projet autopadlet permettant de transferer automatiquement des photos d'une discussion whatsapp a un padlet.

!!!ATTENTION!!! Autopadlet est encore en cours de developpement, le code python n'a pas encore ete rendu propre, lisible, et explique. De plus, ce README est encore incomplet.

Quelques informations par rapport au programme:
-Autopadlet necessite les librairies python selenium, time, os, pyautogui, csv, et sys pour fonctionner.

-Le fichier autopadlet.py est le fichier principal a executer avec python

-Avant d'utiliser autopadlet il faut s'etre connecte a whatsapp web avec chrome (un autre navigateur necessiterait des modifications du code). Il faut aussi avoir entre le lien pour acceder au padlet directement dans le code autopadlet.py. Il faut ensuite modifier les variables categories, catcodes, catids pour qu'elles correspondent a votre padlet (instructions pour catids plus tard). Il faut aussi changer la valeur de discussionname pour qu'elle corresponde a la discussion whatsapp que vous voulez utiliser. Enfin, veuillez verifier que les #div names correspondent a celles qui sont actuellement utilisees par whatsapp (plus d'infos sur ou les trouver plus tard).

-Il est preferable d'executer l'algorithme sur un ordinateur n'etant pas utilise regulierement et ayant une connexion internet stable (j'utilise par exemple un raspberry pi que je n'utilise pas ou peu et sur lequel l'algorithme tourne 24h/24). L'algorithme est capable de gerer des pertes de connexion internet. Il faut aussi noter que whatsapp web a tendance a faire se vider plus rapidement la batterie du telephone auquel le compte whatsapp qui y est associe est connecte.
