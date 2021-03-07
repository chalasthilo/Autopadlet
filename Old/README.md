# Autopadlet
On peut trouver ici le code source du projet autopadlet permettant de transferer automatiquement des photos d'une discussion whatsapp a un padlet.

!!!ATTENTION!!! Autopadlet est encore en cours de developpement. De plus, ce README est encore incomplet.

Quelques informations par rapport au programme:

-Autopadlet necessite les librairies python selenium, time, os, pyautogui, csv, et sys pour fonctionner.

-Il faut un ordinateur sous linux pour que l'algorithme fonctionne (quelques adaptations seraient necessaires pour utiliser d'autres OS)

-Le fichier autopadlet.py est le fichier principal a executer avec python

-L'algorithme fonctionne sur des padlets de type "etagere" ("shelf" en anglais) (celui avec l'image bleue quand on cree le padlet)

-Avant d'utiliser autopadlet il faut s'etre connecte a whatsapp web avec chrome (un autre navigateur necessiterait des modifications du code). Il faut aussi avoir entre le lien pour acceder au padlet directement dans le code autopadlet.py. Il faut ensuite modifier les variables categories, catcodes, catids pour qu'elles correspondent a votre padlet (instructions pour catids plus tard). Il faut aussi changer la valeur de discussionname pour qu'elle corresponde a la discussion whatsapp que vous voulez utiliser. Enfin, veuillez verifier que les #div names correspondent a celles qui sont actuellement utilisees par whatsapp (plus d'infos sur ou les trouver plus tard). Il faut enfin changer quelques autres elements relatifs aux chemins des fichiers utilises.

  -Il est preferable d'executer l'algorithme sur un ordinateur n'etant pas utilise regulierement et ayant une connexion internet stable (j'utilise par exemple un raspberry pi que je n'utilise pas ou peu et sur lequel l'algorithme tourne 24h/24). L'algorithme est capable de gerer des pertes de connexion internet. Il faut aussi noter que whatsapp web a tendance a faire se vider plus rapidement la batterie du telephone auquel le compte whatsapp qui y est associe est connecte. On peut par exemple utiliser un vieux telephone ne servant plus sur lequel on cree un autre profil whatsapp (pas besoin d'un deuxieme abonnement telephonique, il suffit de "creer" un faux numero de telephone. Explications ici par exemple: https://sendapp.live/fr/2020/04/08/numero-virtuel-pour-activer-whatsapp/).


Mise en place:

1. Telecharger autopadlet (tous les fichiers .py et .csv) dans un meme dossier, creer un dossier nomme "chromedata" dans le dossier ou vous avez mis les fichiers, et installer les librairies necessaires si besoin.

2. Choisir la discussion whatsapp ou vous voulez utiliser autopadlet.

3. Ouvrir le fichier autopadlet.py dans un editeur de texte (VSCode, Geany, Atom,...).

4. Remplacer le lien de la ligne 22 par celui de votre padlet.

5. Remplacer le nom de la discussion ligne 25 par le nom de votre discussion whatsapp (faire attention a avoir ' puis " puis le nom de la discussion puis " puis ') Exemple: discussionname = '"Discussion"'.

6. Verifiez si les noms des classes de whatsapp web sont correctes et les remplacer si necessaire (c.f. Noms des classes whatsapp web ci dessous).

7. Dans la ligne 47, remplacer les noms des categories pour qu'ils correspondent a ceux de votre padlet. Vous pouvez ajouter ou enlever des categories si necessaire. Ces categories correspondent aux colonnes du padlet.

8. Dans la ligne 48, remplacer les codes des categories par des codes de votre choix. Il faut imperativement avoir un code par categorie. Les codes de chaque categorie correspondent a la categorie ayant le meme indice dans la liste (le premier code est celui de la premiere categorie,...). Dans le code initial le code C1 correspond a la categorie "First column".

9. Dans la ligne 49, remplacer les "section-xxxxxxxx" par ceux de votre padlet (c.f. Noms des classes pour les categories du padlet ci dessous).

10. Dans la ligne 62, remplacer le chemin "/home/pi/Desktop/Projet_Transfert_Auto_Padlet/chromedata/Default" par le chemin du dossier ou vous avez mis les fichiers d'autopadlet (ajouter /chromedata/Default a la fin comme dans le chemin preexistant).

11. Dans la ligne 64, remplacer le chemin "/home/pi/.config/chromium/Default" par le chemin menant au dossier "Default" de votre installation de chrome (le chemin devrait ressembler au preexistant avec quelques variations). Remplacer ensuite le chemin "/home/pi/Desktop/Projet_Transfert_Auto_Padlet/chromedata" par celui menant a votre dossier avec les fichiers d'autopadlet (ce chemin sera le meme que celui de la ligne 62 sauf sans le "/Default" a la fin.

12. Dans la ligne 69, remplacer le chemin "/home/pi/Desktop/Projet_Transfert_Auto_Padlet/chromedata" par celui correspondant a votre ordinateur (c'est le meme chemin que le deuxieme chemin utilise dans la ligne 64).

13. Dans la ligne 73 et la ligne 81, remplacer le chemin "/usr/lib/chromium-browser/chromedriver" par celui correspondant a votre installation chrome (chemin menant au dossier "chromedriver").

14. Sauvegarder et fermer le fichier autopadlet.

15. Ouvrir le fichier whatsappweb.py dans votre editeur de texte.

16. Dans la ligne 105, changer le message pour qu'il corresponde a votre padlet. On pourra ecrire par exemple: "Bonjour, voici la liste des catégories dans le padlet: [DS, DM et interros: code = DSDM],[Progression Prévue: code = PP],[Chapitre {nombre du chapitre} cours: code = C{nombre du chapitre}C (ex: cours chapitre 1: code = C1C)],[[Chapitre {nombre du chapitre} exercices: code = C{nombre du chapitre}EX (ex: exercices chapitre 1: code = C1EX)]".

17. Dans la ligne 107, changer le lien dans le message pour que ce soit celui de votre padlet.

18. Sauvegarder et fermer le fichier.

19. Ouvrir chrome puis naviguer vers la page "web.whatsapp.com".

20. Scanner le QR-code avec votre telephone.

21. Fermer chrome.

22. Executer le fichier autopadlet.py avec python (python3 autopadlet.py dans le terminal linux)
