# Autopadlet
On peut trouver ici le code source du projet autopadlet permettant de transferer automatiquement des photos d'une discussion whatsapp a un padlet.

!!!ATTENTION!!! Autopadlet est encore en cours de developpement. De plus, ce README est encore incomplet.

Quelques informations par rapport au programme:

-Autopadlet necessite les librairies python selenium, time, os, pyautogui, json, csv, et sys pour fonctionner.

-Il faut un ordinateur sous linux pour que l'algorithme fonctionne (quelques adaptations seraient necessaires pour utiliser d'autres OS)

-Le fichier autopadlet_V2.py est le fichier principal a executer avec python

-L'algorithme fonctionne sur des padlets de type "etagere" ("shelf" en anglais) (celui avec l'image bleue quand on cree le padlet)

-Avant d'utiliser autopadlet il faut s'etre connecte a whatsapp web avec chrome (un autre navigateur necessiterait des modifications du code). Il faut ensuite modifier/creer le fichier discussionswithpadlets.json a l'aide du script discussion_manager.py (instructions plus tard). Enfin, veuillez verifier que les #div names correspondent a celles qui sont actuellement utilisees par whatsapp (plus d'infos sur ou les trouver plus tard). Il faut enfin changer quelques autres elements relatifs aux chemins des fichiers utilises.

-Il est preferable d'executer l'algorithme sur un ordinateur n'etant pas utilise regulierement et ayant une connexion internet stable (j'utilise par exemple un raspberry pi que je n'utilise pas ou peu et sur lequel l'algorithme tourne 24h/24). L'algorithme est capable de gerer des pertes de connexion internet. Il faut aussi noter que whatsapp web a tendance a faire se vider plus rapidement la batterie du telephone auquel le compte whatsapp qui y est associe est connecte. On peut par exemple utiliser un vieux telephone ne servant plus sur lequel on cree un autre profil whatsapp (pas besoin d'un deuxieme abonnement telephonique, il suffit de "creer" un faux numero de telephone. Explications ici par exemple: https://sendapp.live/fr/2020/04/08/numero-virtuel-pour-activer-whatsapp/).


Mise en place:

1. Telecharger autopadlet (tous les fichiers .py et .csv) dans un meme dossier, creer un dossier nomme "chromedata" dans le dossier ou vous avez mis les fichiers, et installer les librairies necessaires si besoin.

2. Choisir les discussions whatsapp ou vous voulez utiliser autopadlet.

3. Ouvrir le fichier discussion_manager.py dans un editeur de texte (VSCode, Geany, Atom,...).

4. Trouver la liste de dictionnaires nommee "discussions". Dans la liste faitez des copier-coller du dictionnaire existant (commencant par "{" et finissant par "}" afin d'avoir autant de dictionnaires que de discussions.

5. Dans chaque dictionnaire, remplacer les valeurs attribuees a "discussionname" et "padletlink" par le nom de la discussion (celui qui est affiche sur whatsapp) et le lien de votre padlet correspondant a cette discussion.

6. Dans chaque dictionnaire, remplacer les noms des categories pour qu'ils correspondent a ceux du padlet attribue a ce dictionnaire (la liste attribuee a "categories"). Vous pouvez ajouter ou enlever des categories si necessaire. Ces categories correspondent aux colonnes du padlet.

8. Dans chaque dictionnaire, remplacer les codes des categories par des codes de votre choix (la liste attribuee a "catcodes"). Il faut imperativement avoir un code par categorie. Les codes de chaque categorie correspondent a la categorie ayant le meme indice dans la liste (le premier code est celui de la premiere categorie,...). Dans le dictionnaire deja present le code C1 correspond a la categorie "First column".

9. Dans chaque dictionnaire, remplacer les "section-xxxxxxxx" par ceux de votre padlet (c.f. Noms des classes pour les categories du padlet ci dessous) (liste attribuee a "catids").

10. Sauvegarder et executer le script "discussion_manager.py".

11. Ouvrir le script autopadlet_V2.py dans l'editeur de texte.

12. Verifiez si les noms des classes de whatsapp web sont correctes et les remplacer si necessaire (c.f. Noms des classes whatsapp web ci dessous).

13. Dans la ligne 91, remplacer le chemin "/home/pi/Desktop/Projet_Transfert_Auto_Padlet/chromedata/Default" par le chemin du dossier ou vous avez mis les fichiers d'autopadlet (ajouter /chromedata/Default a la fin comme dans le chemin preexistant).

14. Dans la ligne 92, remplacer le chemin "/home/pi/.config/chromium/Default" par le chemin menant au dossier "Default" de votre installation de chrome (le chemin devrait ressembler au preexistant avec quelques variations). Remplacer ensuite le chemin "/home/pi/Desktop/Projet_Transfert_Auto_Padlet/chromedata" par celui menant a votre dossier avec les fichiers d'autopadlet (ce chemin sera le meme que celui de la ligne 91 sauf sans le "/Default" a la fin.

15. Dans la ligne 94, remplacer le chemin "/home/pi/Desktop/Projet_Transfert_Auto_Padlet/chromedata" par celui correspondant a votre ordinateur (c'est le meme chemin que le deuxieme chemin utilise dans la ligne 92).

16. Dans la ligne 95 et la ligne 100, remplacer le chemin "/usr/lib/chromium-browser/chromedriver" par celui correspondant a votre installation chrome (chemin menant au dossier "chromedriver").

17. Sauvegarder et fermer le fichier autopadlet.

18. Ouvrir le fichier whatsappweb.py dans votre editeur de texte.

19. Sauvegarder et fermer le fichier.

20. Ouvrir chrome puis naviguer vers la page "web.whatsapp.com".

21. Scanner le QR-code avec votre telephone.

22. Fermer chrome.

23. Executer le fichier autopadlet_V2.py avec python (python3 autopadlet_V2.py dans le terminal linux)
