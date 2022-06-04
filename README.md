# Text2Test
Testing Framework that implements BDD through Gherkin syntax and makes use of predefined keywords to generate web automated test cases using PyTest and Selenium Webdriver

## Installation

Download locally the git repository.

Run commands:
1. Function runtext2test {python "path\to\controller.py" $args}
2. Set-Alias -Name text2test -Value runtext2test

## Usage

Create feature files inside the "features" folder.

Example:
- Feature: run a login test case with background

    - Background:
        - Given we open WEBSITE 'https://www.amazon.com/'

    - Scenario: login
        - Given we open WEBSITE 'https://www.clientam.com/sso/Login'
        - When we CLICK 'user_name'
        - And we TYPE 'user_name' 'uname'
        - And we CLICK 'password'
        - And we TYPE 'password' 'pass'
        - And we CLICK 'submitForm'
        - Then an ERROR 'ERRORMSG' 'Invalid username password combination' will be raised

Keywords have corresponding Selenium code inside the 'code.json' file.

Keywords usage:
    - WEBSITE + 'link': opens the link
    - CLICK + 'id': clicks on the specified element 
    - TYPE + 'id' + 'text': types test into the specified element
    - TITLE + 'text': verifies title is equal to text
    - SCREENSHOT + 'name': takes screenshot and saves it as name
    - ERROR + 'id' + 'text':  verifies the error with id is equal to text

Feel free to update the 'code.json' file to add keywords for your specific needs.

Run text2test with parameters:
 - Syntax: text2test [-t|all|run|h] [--help]
 - options:
 - h:     Print this Help.
 - help:  Print this Help.
 - t:     Generate a test from a specific feature file.
 - all:   Generate tests from all feature files inside features folder.
 - run:   Execute generated test cases and generate a report.

# Text2Test
Cadre de test qui implémente BDD via la syntaxe Gherkin et utilise des mots clés prédéfinis pour générer des cas de test automatisés Web à l'aide de PyTest et de Selenium Webdriver

## Installation

Téléchargez localement le référentiel git.

Exécutez les commandes:
1. Function runtext2test {python "path\to\controller.py" $args}
2. Set-Alias ​​-Name text2test -Value runtext2test

## Utilisation

Créez des fichiers de fonctionnalités dans le dossier "features".

Exemple:
- Fonctionnalité: exécutez un cas de test de connexion avec un arrière-plan

    - Arrière plan:
        - Étant donné que nous ouvrons le SITE WEB 'https://www.amazon.com/'

    - Scénario : connexion
        - Étant donné que nous ouvrons le SITE 'https://www.clientam.com/sso/Login'
        - Lorsque nous CLIQUEZ sur 'user_name'
        - Et on TAPE 'user_name' 'uname'
        - Et on CLIQUE sur 'mot de passe'
        - Et on TAPE 'password' 'pass'
        - Et nous CLIQUEZ sur 'submitForm'
        - Ensuite, une ERREUR 'ERRORMSG' 'Combinaison de mot de passe de nom d'utilisateur invalide' sera générée

Les mots-clés ont le code Selenium correspondant dans le fichier 'code.json'.

Utilisation des mots-clés :
    - WEBSITE + 'lien' : ouvre le lien
    - CLICK + 'id' : clique sur l'élément spécifié
    - TYPE + 'id' + 'text' : les types testent dans l'élément spécifié
    - TITLE + 'texte' : vérifie que le titre est égal au texte
    - SCREENSHOT + 'nom' : prend une capture d'écran et l'enregistre sous le nom
    - ERROR + 'id' + 'text' : vérifie l'erreur avec id est égal à text

N'hésitez pas à mettre à jour le fichier 'code.json' pour ajouter des mots-clés adaptés à vos besoins spécifiques.

Exécutez text2test avec les paramètres :
 - Syntaxe : text2test [-t|all|run|h] [--help]
 - option :
 - h : imprimez cette aide.
 - help : imprimez cette aide.
 - t : génère un test à partir d'un fichier de fonctionnalité spécifique.
 - all : génère des tests à partir de tous les fichiers de fonctionnalités dans le dossier de fonctionnalités.
 - run : Exécute les cas de test générés et génère un rapport.