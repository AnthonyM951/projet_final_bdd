Usage
=====

.. _installation:

utilisation
------------

1. Dans "projet_final" > `python mainFast.py`

2. Dans les deux cas, l'adresse est :  `http://127.0.0.1:5000` ou `http://localhost:5000`

Fonctionnalités principales pour FastAPI
-----------------------------------------


1. **Obtenir la liste des pays** : GET /api/onu/postgresql/getcountries/

2. **Signatures par Date** : GET /api/onu/postgresql/getsignbydate/

3. **Liste des Traités** : GET /api/onu/postgresql/get_treaty/

4. **Statut par Signature** : GET /api/onu/postgresql/status_by_signature/{signature_id}

5. **Recherche par Texte Intégral** : GET /api/onu/postgresql/searchPleinTextDiplomat/{keyword}

6. **Créer un Utilisateur** : POST /api/onu/postgresql/create_user

7. **Créer un Rôle** : POST /api/onu/postgresql/create_role

8. **Attribuer des Privilèges** : POST /api/onu/postgresql/assign_privileges

9. **Attribuer un Rôle** : POST /api/onu/postgresql/assign_role



fastAPI donne la posisbilité d'accéder à une documentation générée automatiquement à partir de ce lien :
`http://127.0.0.1:5000/docs`

![img.png](utils/imgFast.png)

