#!/usr/bin/env python
# coding: utf-8

# ## <div id="Pour_commencer_Python">3. Pour commencer Python</div>
# 
# Comme nous l'avons vu, python est un langage de programmation assez permissif. Mais ce dernier n'en est pas moins facile d'accès si on a pas l'habitude de programmer. Dans le cadre de cette formation, l'ensemble de l'installation de python et des modules utilisées pour faire fonctionner le code est téléchargé sur le serveur sur lequel vous êtes connecté. Pour utiliser python sur votre ordinateur voici deux façons pour l'installer.
# 
# ### <div id="installation_anaconda">3. 1. Installation avec <i>Anaconda</i></div>
# 
# <a href="https://www.anaconda.com/">Anaconda</a> est un logiciel qui permet d'installer et de gérer python et ses *dépendances* (cad les fichiers que l'on charge pour utiliser python) avec une interface graphique accessible. De plus, Anaconda met à disposition un certain nombre d'IDLE, c'est-à-dire de logiciel pour éditer votre futur code source, et propose la gestion des packages pour chacun de vos projets. Anaconda ne se limite pas qu'à l'utilisation de Python, il permet également d'installer R et Rstudio, ainsi que d'autres logiciels faisant parties de l'éco-système de la *data-science*.En somme, Anaconda est très pratique si vous n'avez jamais ouvert un terminal ou un invité de commande de votre vie. 
# 
# Une fois le fichier d'installation téléchargé et exécuté, python est installé sur votre ordinateur ainsi que plusieurs applications ppour l'utiliser :
# 
# <div align="center"><img src="capture_anaconda.PNG"/></div>
# 
# En particulier, vous pourrez utiliser Spyder pour l'édition de votre code, mais aussi la suite Jupyter sur laquelle nous reviendrons.
# 
# <div class="alert alert-success" role="alert"><b>Anaconda</b> a plusieurs <b>avantages</b> et <b>inconvénients</b>:
# <ul> <li>Le plus gros avantage est le fait de pouvoir gérer tout ce qui est relatif à python depuis cette interface graphique : la gestion des librairires, des environnements virtuels,...</li>
# <li>C'est également ce qui en constitue sont inconvénients dans la mesure où toutes les fonctions natives de python passent pas Anaconda : en particulier vous n'utiliserez pas la fonction 'pip' pour l'installation, mais la fonction 'conda', ce qui va faire que vous n'utiliserez jamais les environnements virtuels proposé par Conda.</li></ul></div>
# 
# De plus, si les lignes de commandes ne vous effraie pas, il est plus recommandable de faire votre propre installation de python et d'installer vos librairies et modules dans votre terminal.
# 
# ### <div id="installation_brute">3. 2. Installation <i>brute</i></div>
# 
# L'installation de python n'est pas beaucoup plus compliqué si l'on utilise les <a href="https://www.python.org/downloads/">fichiers d'installation</a> du site officiel. Si vous utilisez les versions dénommées "installer", vous n'aurez qu'à double-cliquez sur le fichier téléchargé et le tour sera joué. Pour vérifier que python est bien installé sur votre ordinateur vous pouvez ouvrir un terminal ou un invité de commande et écrire "python -V". Le résultat attendu est la version que vous avez installé de python : 
# 
# <div align="center"><img src="capture_vers_py.PNG"/></div>
# 
# Le résultat attendu est le même pour le terminal sous Mac Os ou sous Linux. Vous pouvez dès à présent utiliser python directement dans votre terminal ou invité de commande : 
# 
# <div align="center"><img src="Capture_python_exec.PNG"/></div>
# 
# Cependant, il n'est pas conseillé d'utiliser python directement dans votre termial : 
# * D'abord parce que vous ne pourrez pas corriger votre code
# * Parce que vous ne pourrez pas l'enregistrer simplement
# * Parce que vous ne bénéficier d'aucun avantage d'un IDLE, même simple (coloriage des parties du codes, auto-complétion,...).
# 
# <div class="alert alert-danger" role="alert"><b>C'est pourquoi il vous faut un IDLE qui vous permettent d'éditer votre code facilement.</b> 
# <br>
# <br>
# C'est outils sont nombreux, et je ne vous ferais pas une liste exhaustive ici, mais vous pouvez vous intéressez à des outils tels que CotEditor (pour MacOs et Linux) ou Notepad++ pour Windows, mais aussi à des logiciels avec beaucoup de fonctionnalités comme VisualCode, ou Pycharm. Tout ces logiciels permettent d'éditer des fichiers textes, c'est-à-dire votre code source, avec plus ou moins de simplicité. Il en existe de très nombreux, bien que ceux utilisés majoritairement pour développement en Python le sont moins (voir <a href="https://wiki.python.org/moin/PythonEditors">ce lien</a> pour une liste des IDE pour Python).C'est-à-vous de voir l'IDLE qui vous convient le mieux.</div>
# 
# ### <div id="Environnement_Jupyter">3. 3. L'environnement Jupyter</div>
# 
# Parmi ces outils et logiciels, on compte **Jupyter**. Il s'agit d'une forme d'**éditeur de code** qui permet, à la fois :
# * D'écrire du code Python fonctionnel et que l'on peut directement exécuter
# * D'écrire du texte comme on pourrait le faire avec un éditeur de texte classique
# 
# Jupyter est un outil particulièrement utile lorsqu'on souhaite expérimenter, effectuer des tests ou écrire rapidement un petit script pour remplir une tâche minimale. Il est également possible d'écrire des programmes plus complexes dans un notebook Jupyter bien que, dans ce cas là, on préférera passer par l'utilisation d'un **IDLE (Environnement de développement)** plus adapté. Dans notre cas, **Jupyter** sera beaucoup plus utile dans la mesure où il permet également de produire des documents propres (exportables en PDF notamment), intégrant le code Python ainsi que des analyses associées, des commentaires ou une documentation de ce même code.
# 
# **Jupyter** se présente sous la forme d'une page web disposant d'un menu dédié et fonctionnant à l'aide de **cellules**. Une cellule peut contenir :
# * Du code Python
# * Du texte, des images, des liens externes (n'importe quel contenu que l'on peut afficher sur un document HTML)
# 
# #### <div id="Environnement_Jupyter">3. 3. 1. Installation et lancement de Jupyter</div>
# 
# Pour installer Jupyter Notebook, vous devrez utiliser `pip` qui est une commande très classique de l'environnement python. `pip`, de la même manière que `conda` pour celles et ceux qui installé anaconda, permet d'installer des librairies supplémentaires à notre environnement python. C'est une fonction très pratique que vous serez souvent amené à utiliser pour installer des librairies spécifiques à vos champs d'étude, ou à vos objets de recherche : un géographe souhaitera rpidement installer des librairies de cartographie, un sociologue des librairies d'analyse de réseaux,...
# 
# Pour installer Jupyter Notebook, il suffit d'écrire cette commande dans votre terminal :
# 
# <div align="center"><img src="Capture_install_nb.PNG"/></div>
# 
# Une fois le processus d'installation terminé, vous pouvez démarrer notebook en tapant la commande `jupyter-notebook` dans votre terminal :
# 
# <div align="center"><img src="Capture_launch_nb.PNG"/></div>
# 
# Cette commande lance un **serveur** sur votre réseau local (localhost), et permet de démarrer Jupyter Notebook. Vous avez donc accès à cette interface, qui vous permet de naviguer dans votre ordinateur, et de créer de nouveaux notebooks. 
# 
# <div align="center"><img src="Capture_nb.PNG"/></div>
# 
# #### <div id="Environnement_Jupyter">3. 3. 2. Quelques astuces</div>
# 
# On peut exécuter une cellule indépendamment d'une autre. Cela permet de découper un code complexe en plusieurs étapes élémentaires successives.
# 
# Si l'on peut utiliser le menu de Jupyter pour exécuter les tâches que l'on souhaite, intégrer les raccourcis au fur et à mesure est bien utile pour gagner du temps. Ainsi, pour **exécuter une cellule**, on peut utiliser la combinaison `shift + entrée`.
# 
# **Quelques raccourcis utiles :**
# 
# |Action|Raccourci|
# |---|---|
# |Exécuter une cellule|`Shift + Entrée` ou `Ctrl + Entrée`|
# |Quitter la cellule sélectionnée|`Esc`|
# |Entrer dans la cellule active|`Entrée`|
# |Passer la cellule en mode code|`Esc + Y`|
# |Passer la cellule en mode texte|`Esc + M`|
# |Copier la cellule active|`Esc + C`|
# |Coller le contenu sur la cellule active|`Esc + V`|
# |Supprimer la cellule sélectionnée|`Esc + D, D`|
# |Afficher tous les raccourcis|`Esc + H`|
# 
# 
# Pour avoir un environnement complet de programmation, on peut également utiliser <a href="https://jupyterlab.readthedocs.io/en/stable/">JupyterLab</a>, qui est installé avec Anaconda.
# 
# #### <div id="Le Markdown">3. 4. Le Markdown</div>
# 
# Les cellules d'un **notebook Jupyter** en **mode texte** interprètent un langage que l'on nomme **Markdown** : il s'agit d'une version du **langage HTML** simplifié qui permet de **structurer des documents textes**.
# 
# Pour passer une cellule en **mode texte**, on peut utiliser le raccourci `Esc + M`.
# 
# Une fois que l'on se situe dans une cellule texte, on peut écrire du texte et le structurer ou ajouter des éléments de mise en forme à l'aide du **Markdown**.
# 
# Il ne s'agira pas ici de faire une liste exhaustive de ce que l'on peut faire avec le Markdown, mais voyons tout de même rapidement quelques éléments utiles.
# 
# Pour insérer des **titres**, on peut utiliser simplement un dièse `#` et entrer à la suite d'un espace le nom que l'on choisit pour ce titre. Selon le nombre de dièses que l'on accole à la suite (sans espace) l'un de l'autre, on pourra définir un titre de niveau différent :
# * `#` : Titre de niveau 1 (le plus grand qui soit)
# * `##` : Titre de niveau 2
# * `###` : Titre de niveau 3
# 
# Pour ajouter des **liens hypertextes**, on peut utiliser une combinaison de crochets et de parenthèses, comme suit :
# * Entre crochets, on insère le texte que l'on veut rendre cliquable : `[Ceci est un lien]`
# * Une fois que l'on a refermé le crochet, on insère tout de suite (sans espace), une paire de parenthèses entre lesquelles on ajoute l'**adresse URL** : `(http://www.mon_site_web.com/mon_lien)`
# 
# Pour insérer ajouter du texte en gras ou en italique, on encadre le segment de texte que l'on souhaite modifier :
# * Entre deux étoiles pour l'italique : `*Ceci est en italique*`
# * Entre quatre étoiles pour le gras (deux avant et deux après) : `**Ceci est en gras**`
# * En gras et en italique, entre trois étoiles (trois avant et trois après) : `***Ceci est en gras et en italique***`
# 
# Pour ajouter des tableaux, c'est un peu plus compliqué, mais c'est possible et cela rend même très bien ! L'idée est d'encadrer les éléments de chaque ligne entre deux **barres obliques** `|`. A chaque fois que l'on veut ajouter une ligne au tableau, on ajoute une nouvelle barre oblique. Une nouvelle colonne est ajoutée à l'aide d'un simple retour à la ligne. Entre la ligne d'en-tête et les lignes du reste du tableau, on ajoute simplement deux barres obliques contenant trois tirets `|---|`. Un exemple de tableau très simple ci-dessous :
# 
# ```markdown
# |Première colonne|Deuxième colonne|
# |---|---|
# |Valeur 1|Valeur 2|
# ```
# 
# |Première colonne|Deuxième colonne|
# |---|---|
# |Valeur 1|Valeur 2|
