# Projet Nations Unies

Documentation brève : [Lien vers la documentation](votre_lien_vers_la_documentation)

Le Projet Nations Unies est une API conçue pour interagir avec la base de données des Nations Unies, couvrant divers aspects liés aux questions mondiales, à la collaboration et aux efforts diplomatiques.

Veuillez noter que cette base de données est entièrement fictive et a été créée à des fins éducatives dans le cadre d'un cours de Master en Ingénierie des Données.

## Objectifs

Les principaux objectifs de ce projet étaient les suivants :

1. Utiliser PostgreSQL avec des mécanismes d'optimisation de requêtes et explorer le concept d'extensions.
2. Implémenter une API interagissant avec la base de données, mettant l'accent sur l'importance d'une modélisation UML correcte en génie logiciel.
3. Acquérir une compréhension approfondie des rôles, des utilisateurs et des privilèges dans la manipulation d'une base de données au sein d'une application.

## Technologies utilisées

- Base de données PostgreSQL en local (ou supabase)
- Python avec le modèle de conception DAO
- Frameworks d'API : Nous avons choisi FastAPI
- Génération de documentation avec Read the Docs

## Démarrage

Pour exécuter l'API localement, suivez ces étapes :

1. Clonez le dépôt.
2. Exécutez soit `python mainFast.py`.
3. Accédez à l'API à l'adresse [http://127.0.0.1:5000](http://127.0.0.1:5000) ou [http://localhost:5000](http://localhost:5000).

## Fonctionnalités

### API Flask

#### Liste des Pays

- Endpoint : `GET /api/onu/postgresql/getcountries/`
- Description : Obtenez la liste des pays depuis la base de données.

#### Signatures par Date

- Endpoint : `GET /api/onu/postgresql/getsignbydate/`
- Description : Obtenez la liste des signatures triées par date depuis la base de données.

#### Liste des Traités

- Endpoint : `GET /api/onu/postgresql/get_treaty/`
- Description : Obtenez la liste des traités depuis la base de données.

#### Statut par Signature

- Endpoint : `GET /api/onu/postgresql/status_by_signature/{signature_id}`
- Description : Obtenez le statut d'une signature spécifique depuis la base de données.

#### Recherche par Texte Intégral

- Endpoint : `GET /api/onu/postgresql/searchPleinTextDiplomat/{keyword}`
- Description : Recherchez des diplomates par texte intégral depuis la base de données.

#### Créer un Utilisateur

- Endpoint : `POST /api/onu/postgresql/create_user`
- Description : Créez un nouvel utilisateur dans la base de données.

#### Créer un Rôle

- Endpoint : `POST /api/onu/postgresql/create_role`
- Description : Créez un nouveau rôle dans la base de données.

#### Attribuer des Privilèges

- Endpoint : `POST /api/onu/postgresql/assign_privileges`
- Description : Attribuez des privilèges à un rôle dans la base de données.

#### Attribuer un Rôle

- Endpoint : `POST /api/onu/postgresql/assign_role`
- Description : Attribuez un rôle à un utilisateur dans la base de données.

### Instructions CORS

```python
# Configuration CORS pour gérer les accès au web service
origins = ["*"]  # Ajoutez ici vos origines autorisées
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
