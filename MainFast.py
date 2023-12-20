import os
import json
from datetime import datetime
import sys
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import sys
import os
from controller import SignatureC, DiplomatC, CountryC, TreatyC, sysadminC
from model import SignatureM, DiplomatM, CountryM, TreatyM


app = FastAPI()

# Configuration CORS pour gérer les accès au web service
origins = ["*"]  # Ajoutez ici vos origines autorisées
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

LOG_FILE_PATH = 'D:/miche/projet_final/utils/logs.json'

Privacy_Policy = '''
Confidentialité et sécurité : Nous accordons la priorité à la protection de vos informations et avons mis en place des mesures de sécurité appropriées pour prévenir l'accès, la divulgation ou la modification non autorisés. Seul le personnel autorisé a accès à ces informations, et il est lié par des obligations de confidentialité.

Restrictions d'accès et d'exploration : L'accès non autorisé à notre application, y compris toute tentative d'exploration de son fonctionnement en accédant à la racine de l'API, est strictement interdit. Toute violation de cette politique de confidentialité ou de nos conditions d'utilisation peut entraîner des mesures disciplinaires, y compris la résiliation du compte et, si nécessaire, des poursuites judiciaires.

Conservation des informations : Nous conservons vos informations aussi longtemps que nécessaire pour atteindre les objectifs énoncés dans cette politique de confidentialité, sauf si une période de conservation plus longue est requise ou autorisée par la loi.

Changements à la politique de confidentialité : Nous nous réservons le droit de modifier cette politique de confidentialité à tout moment. Tous les changements seront effectifs dès leur publication sur notre site Web ou dans l'application. Il est de votre responsabilité de consulter régulièrement cette politique de confidentialité pour toute mise à jour.

Consentement : En utilisant notre application, vous consentez à la collecte, à l'utilisation et à la divulgation de vos informations conformément à cette politique de confidentialité.

Dernière mise à jour : 30/11/2023
'''

@app.get('/', response_model=dict)
async def start():
    """
    Point de départ de l'API.
    """
    return {'Notice': "L'API est protégée, vous ne pouvez rien faire.",
            'Un message pour vous ':"Bonjour cher développeur/utilisateur, BIENVENUE dans la politique de confidentialité de lvmh_sephora",
            'Attention':"Nous collectons certaines informations, y compris votre adresse IP et votre adresse MAC, à des fins de dépannage. Ces informations sont collectées automatiquement et anonymement et ne sont pas utilisées pour vous identifier personnellement sauf en cas de problème technique.",
            'Politique de confidentialité':Privacy_Policy}


@app.get('/api/onu/postgresql/getcountries/')
async def get_countries():
    """
    Obtenir la liste des pays.
    @return: Liste des pays au format JSON.
    """
    countriesc = CountryC.CountryController.view_all_countries()

    print(countriesc)

    liste_countries = []

    if type(countriesc) == list:
        for country_ in countriesc:
            country = {
                "countryId": country_.getCountryId(),
                "name": country_.getCountry_name(),
                "capital": country_.getCapital(),
                "population": country_.getPopulation(),
                "area": country_.getArea()
            }
            liste_countries.append(country)

        return {'response': liste_countries}

    return {'response': countriesc}


@app.get('/api/onu/postgresql/getsignbydate/')
async def get_signatures_by_date():
    """
    Obtenir la liste des signatures triées par date.
    @return: Liste des signatures triées au format JSON.
    """
    list_signatures_sorted_by_date = SignatureC.SignatureController.sortSignatureByDate()

    liste_signatures = []

    if type(list_signatures_sorted_by_date) == list[SignatureM.Signature]:
        for s in list_signatures_sorted_by_date:
            signature = {
                "signature_id": s.getSignatureId(),
                "treaty_id": s.getTreatyId(),
                "country_one": s.getCountryOne(),
                "country_two": s.getCountryTwo(),
                "date": s.getDate(),
                "description": s.getDescription(),
                "status": s.getStatus()
            }
            liste_signatures.append(signature)

        return {'response': liste_signatures}

    else:
        return {'response': list_signatures_sorted_by_date}


@app.get('/api/onu/postgresql/get_treaty/')
async def get_treaty():
    """
    Obtenir la liste des traités.
    @return: Liste des traités au format JSON.
    """


    list_treaties = TreatyC.TreatyController.view_all_treaties()

    if type(list_treaties) == list:
        response_list = []

        for treaty in list_treaties:
            treaty_dict = {
                "treaty_id": treaty.getTreatyId(),
                "name": treaty.getName()
            }
            response_list.append(treaty_dict)

        return {'response': response_list}

    else:
        return {'response': list_treaties}



@app.get('/api/onu/postgresql/status_by_signature/{signature_id}')
async def get_status_by_signature(signature_id: int):
    """
    Obtenir le statut par signature.
    @param signature_id: Identifiant de la signature.
    @return: Statut de la signature au format JSON.
    """
    try:
        status: str | None = SignatureC.SignatureController.get_status_by_signature(signature_id)

        if status is not None:
            return {'response': {'signature_id': signature_id, 'status': status}}
        else:
            raise HTTPException(status_code=404, detail=f"Signature with id {signature_id} not found.")

    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@app.get('/api/onu/postgresql/searchPleinTextDiplomat/{keyword}')
async def search_plein_text_diplomat(keyword: str):
    """
    Rechercher des diplomates par texte intégral.
    @param keyword: Mot-clé pour la recherche.
    @return: Liste des diplomates correspondants au format JSON.
    """

    diplomat_resultats: str | list[DiplomatM.Diplomat] = DiplomatC.DiplomatController.search_product_by_name(keyword)

    if type(diplomat_resultats) == list:
        liste_diplomats = []

        for res in diplomat_resultats:
            diplomat_dict = {
                "diplomat_id": res.get_diplomat_id(),
                "diplomat_name": res.get_diplomat_name(),
                "country_id": res.get_Diplomatcountry()
                # Add other attributes as needed
            }

            liste_diplomats.append(diplomat_dict)

        return {'response': liste_diplomats}

    return {'response': diplomat_resultats}



@app.post('/api/onu/postgresql/create_user')
async def create_user(data: dict):
    """
    Créer un nouvel utilisateur.
    @return: Réponse JSON indiquant le statut de la création.
    """
    try:
        password = data.get('password')
        username = data.get('username')
        print(password)

        response = sysadminC.SysAdmin.creerUnUser(password, username)

        if response == "ERROR":
            return {"response": "Erreur lors de la création de l'utilisateur."}
        else:
            return {"response": response}

    except Exception as e:
        print(f"Erreur lors de la création de l'utilisateur : {e}")
        return {"response": "Erreur interne du serveur."}


@app.post('/api/onu/postgresql/create_role')
async def create_role(data: dict):
    """
    Créer un nouveau rôle.
    @return: Réponse JSON indiquant le statut de la création.
    """
    try:
        role = data.get('role')

        response = sysadminC.SysAdmin.creerUnRole(role)

        if response == "ERROR":
            return {"response": "Erreur lors de la création du rôle."}
        else:
            return {"response": response}

    except Exception as e:
        print(f"Erreur de creation du rôle: {e}")
        return {"response": "Erreur interne du serveur."}

@app.post('/api/onu/postgresql/assign_privileges')
async def assign_privileges(data: dict):
    """
    Attribuer des privilèges à un rôle.
    @param data: Réponse JSON contenant les détails des privilèges
    @return: Réponse JSON indiquant le statut de l'attribution.
    """
    try:
        privileges = data.get('privileges')
        tables = data.get('tables')
        roles = data.get('roles')

        response = sysadminC.SysAdmin.privilege_Role(privileges, tables, roles)

        if response == "ERROR":
            return {"response": "Erreur lors de l'attribution des privilèges."}
        else:
            return {"response": response}

    except Exception as e:
        print(f"Erreur lors de l'attribution des privilèges : {e}")
        return {"response": "Erreur interne du serveur."}


@app.post('/api/onu/postgresql/assign_role')
async def assign_role(data: dict):
    """
    Attribuer un rôle à un utilisateur.
    @param data: Réponse JSON contenant les détails de l'attribution du rôle
    @return: Réponse JSON indiquant le statut de l'attribution.
    """
    try:
        user = data.get('user')
        roles = data.get('roles')

        response = sysadminC.SysAdmin.attribution_Role(user, roles)

        if response == "ERROR":
            return {"response": "Erreur lors de l'attribution des rôles."}
        else:
            return {"response": response}

    except Exception as e:
        print(f"Erreur lors de l'attribution des rôles : {e}")
        return {"response": "Erreur interne du serveur."}




if __name__ == '__main__':
    # Exécutez l'application FastAPI
    import uvicorn
    uvicorn.run(app, host="localhost", port=5000)
