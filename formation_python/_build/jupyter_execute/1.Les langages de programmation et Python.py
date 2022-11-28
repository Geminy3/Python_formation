#!/usr/bin/env python
# coding: utf-8

# ## <div id="Les_langages_de_programmation_et_Python">2. Les langages de programmation et Python</div>
# 
# Avant de se lancer dans python en particulier, il est important de comprendre ce que fait un langage de programmation à l'ordinateur. Pour certains problèmes, des solutions n'existent pas, et cela peut être lié aussi bien au langage de programmation, à votre ordinateur, qu'à python lui même. C'est en comprenant un minimum cette théorie que l'on se repère également au mieux dans les forums de discussions, et qu'on peut au mieux décrire nos problèmes. 
# 
# ### <div id="C_est_quoi_un_langage_de_programmation_?">2. 1. C'est quoi un langage de programmation ?</div>
# 
# Un **langage de programmation** est un type specifique de <a href="https://fr.wikipedia.org/wiki/Langage_informatique">**langage informatique**</a>, puisqu'il permet de manipuler des informations (qu'on appelle aussi des *inputs*) au travers d'un ensemble de procédés pour produire des résultats (des *outputs*). En somme, un langage de programmation permet de créer des recettes de cuisine qui vont se faire toute seule. C'est à vous d'écrire la recette pour que l'ordinateur puisse :
# * Sélectionner l'information à traiter (les ingrédients)
# * Transformer l'information comme vous le souhaitez (la recette)
# * Afficher les résultats (le gateau)
# 
# Ce travail est ce qu'on appelle de **l'algorithmie**, c'est à dire un enchaînement d'opération à partir d'une entrée, et qui donne un résultat (ou non) en sortie. L'ensemble des tâches et des manipulations est ce qu'on appelle également un **programme**.
# 
# Il existe une grande quantité de langage de programmation, qui sont plus ou moins adaptés à des tâches spécifiques ou généralistes. Vous avez peut-être déjà entendu parler de R, un langage spécialisé dans la statistique, ou encore javascript, qui permet en particulier de générer des pages internet dynamique.
# 
# Pour fonctionner, un langage repose sur un ordinateur, qui comprend - plus ou moins bien - ce que le langage veut dire pour réaliser les instructions qu'on lui demande. En pratique, le langage est transformé en instruction très simple (pour lui !) que l'ordinateur peut interpréter : c'est ce qu'on appelle **du lanage machine**. 
# 
# <div align="center"><img src="https://i0.wp.com/le-m-verbatem.fr/wp-content/uploads/2020/06/100972028_975734276215792_3564176561886199808_n.png?resize=768%2C355&ssl=1" width="800" height="600" alt="Ce n'est pas très lisible"></div>
# 
# A l'inverse de Néo et des enfants de Sion, ce langage est complètement illisible et encore moins écrivable puisqu'il s'agit d'un ensemble de bits (de suite de huit 0 ou 1) collés les uns à la suite des autres. Il faut ainsi un traducteur entre le langage que nous écrivons, et les instructions que la machine peut exécuter : on parle alors de **compilateur**, ou **d'interprète**. Ces programmes permettent de convertir nos fichiers python en **instructions exécutables par le processeur**, et donc par l'ensemble de l'ordinateur. 
# 
# ### <div id="Et_les_langage,_ils_ont_des_niveaux_?">2. 2.Et les langage, ils ont des niveaux ?</div>
# 
# En fonction de la proximité avec le langage machine, on parle de **niveau de langage** pour les langages informatiques. En théorie, seul le langage assembleur pourrait être considéré de bas niveau, car il est très proche du fonctionnement du langage machine (il nécessite cependant d'être interprété par la machine, comme nous l'avons vu précédemment). Mais dans la pratique, on parle de langage de bas niveau pour les langages de progammation qui sont les moins abstraits pour l'ordinateur, c''est-à-dire les langages les plus abstraits pour nous. En pratique, plus le langage est rigoureux et demande des efforts de définition des opérations, plus on considère qu'il est de bas niveaux. 
# 
# Et vous vous demandez, "pourquoi est-ce que j'ai besoin de connaître ces informations ?", "déjà que je ne sais pas utiliser python, j'ai pas besoind e savoir comment fonctionne l'assembleur !". Détrompez-vous, parce que python a un statut un peu particulier au sein de la pratique des langages de programmation. 
# 
# Python est donc un langage de haut niveau, ni trop proche de l'écriture litérale des actions que l'on souhaite réaliser, ni trop abstrait pour nous, ce qui lui offre une grande qualité dans sa **syntaxe**, c''est-à-dire la manière d'écrire des instructions en python. Sa deuxième grande force (mais qui est à terme une faiblesse), est le fait que vous n'avez pas besoind de compiler le code pour que vous puissez exécuter un programme, on dit que Python est un langage **pré-compilé**. La troisième qualité de Python est sa polyvalence : il n'est optimisé pour aucune application, mais sa lisibilité et son accessibilité en ont fait le langage le plus utilisé dans le monde, ce qui fait que la plupart des ressource disponibles pour programmer son disponible sur python.
