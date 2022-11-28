#!/usr/bin/env python
# coding: utf-8

# ## <div id="Pour_commencer_Python">3. Pour commencer Python</div>
# 
# Comme nous l'avons vu, python est un langage de programmation assez permissif. Mais ce dernier n'en est pas moins facile d'accès si on a pas l'habitude de programmer. Dans le cadre de cette formation, l'ensemble de l'installation de python et des modules utilisées pour faire fonctionner le code est téléchargé sur le serveur sur lequel vous êtes connecté. Pour utiliser python sur votre ordinateur voici deux façons pour l'installer.
# 
# ### <div id="installation_anaconda">3. 1. Installation avec <i>Anaconda</i></div>
# 
# 
# 
# ### <div id="installation_brute">3. 2. Installation <i>brute</i></div>
# 
# 
# ### <div id="Environnement_Jupyter">3. 3. L'environnement Jupyter</div>
# 
# Parmi ces outils, on compte **Jupyter**. Il s'agit d'une forme d'**éditeur de code** qui permet, à la fois :
# * D'écrire du code Python fonctionnel et que l'on peut directement exécuter
# * D'écrire du texte comme on pourrait le faire avec un éditeur de texte classique
# 
# Jupyter est un outil particulièrement utile lorsqu'on souhaite expérimenter, effectuer des tests ou écrire rapidement un petit script pour remplir une tâche minimale. Il est également possible d'écrire des programmes plus complexes dans un notebook Jupyter bien que, dans ce cas là, on préférera passer par l'utilisation d'un **IDE (Environnement de développement)** plus adapté. Il en existe de très nombreux, bien que ceux utilisés majoritairement pour développement en Python le sont moins (voir <a href="https://wiki.python.org/moin/PythonEditors">ce lien</a> pour une liste des IDE pour Python).
# 
# Dans notre cas, **Jupyter** sera beaucoup plus utile dans la mesure où il permet également de produire des documents propres (exportables en PDF notamment), intégrant le code Python ainsi que des analyses associées, des commentaires ou une documentation de ce même code.
# 
# **Jupyter** sous la forme d'une page web disposant d'un menu dédié et fonctionnant à l'aide de **cellules**. Une cellule peut contenir :
# * Du code Python
# * Du texte, des images, des liens externes (n'importe quel contenu que l'on peut afficher sur un document HTML)
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
# #### <div id="Le Markdown">2. 2. 2. Le Markdown</div>
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
