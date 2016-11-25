# outils-GALA

outils-GALA est une série d'outils qui permettent de produire un fichier XML conforme aux exigences de Bibliothèque et Archives nationales du Québec ([BAnQ](thhp://www.banq.qc.ca)).

Le script gala-csv2xml.py produit le fichier XML à partir d'un fichier CSV.

Le script gala-validateurxsd.py valide le fichier XML contre le [schéma](http://www.banq.qc.ca/documents/archives/archivistique_ged/gala/Regle_format_XSD.xsd) publié par BAnQ.

##Préalable
Instructions complètes à venir.

1. Produire le calendrier de conservation avec un chiffrier selon le modèle (voir CalendrierConservationExemple.csv).
2. Enregistrer le calendrier de conservation en format csv (le programme s'attend à ce qu'il se nomme CalendrierConservation.csv).
3. Utiliser le script gala-csv2xml pour créer le fichier XML.
4. Utiliser le script gala-validateurxsd pour valider votre fichier XML.
5. Suivre les procédures de BAnQ pour [soumettre un calendrier de conservation avec GALA](http://www.banq.qc.ca/archives/archivistique_gestion/services_partenaires/organismes_publics/soumission.html), lien  consulté le 2016-11-25.

##Utilisation
Pour lancer le script, en ligne de commande : `$ python gala-csv2xml.py CalendrierConservation.csv`

Le fichier produit se nomme `CalendrierConservationGala.xml`.

##Problèmes connus
- Le programme gala-csv2xml.py créer une ligne même si aucune valeur n'est inscrite dans le fichier csv (exemple, si le champs « Remarque semi-actif » n'est pas renseigné il existera tout de même une ligne avec la chaîne `<REM_PERIOSMACT></REM_PERIOSMACT>`). Voir : http://www.banq.qc.ca/documents/archives/archivistique_ged/gala/Exemple_regles_format_xml.xml consulté le 2015-07-02.

##Liens
- [Soumission d'un calendrier de conservation avec GALA](http://www.banq.qc.ca/archives/archivistique_gestion/services_partenaires/organismes_publics/soumission.html), lien consulté le 2016-11-25.
