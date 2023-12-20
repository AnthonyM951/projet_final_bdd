from dao.DiplomatDAO import DiplomatDAO
from model.DiplomatM import Diplomat
from model.CountryM import Country

class DiplomatController:

    @staticmethod
    def view_all_diplomats():
        '''
        View all diplomats.
        @return: List of diplomats.
        '''
        try:
            diplomat_dao = DiplomatDAO()
            diplomats = diplomat_dao.find_all()

            if diplomats is None:
                return "ERROR"

            return diplomats

        except Exception as e:
            print(f'Error_DiplomatController.view_all_diplomats() ::: {e}')

        return None

    @staticmethod
    def view_one_diplomat(diplomat_id):
        '''
        View a specific diplomat.
        @param diplomat_id: ID of the diplomat.
        @return: Specific diplomat.
        '''
        try:
            diplomat_dao = DiplomatDAO()
            diplomat = diplomat_dao.find_one(diplomat_id)

            if diplomat is None:
                return "ERROR"

            return diplomat

        except Exception as e:
            print(f'Error_TreatyController.view_one_diplomat() ::: {e}')

        return None

    @staticmethod
    def add_one_diplomat(name,countryId:int):
        '''
        Add a diplomat.
        @param diplomat_id: ID of the diplomat.
        @param name: Name of the diplomat.
        @param countryId: Id of referent Country.
        '''
        try:
            diplomat_dao = DiplomatDAO()
            obj_diplomat = Diplomat()
            c1 = Country()

            c1.setCountryId(countryId)

            obj_diplomat.set_Diplomatcountry(c1)
            obj_diplomat.setName(name)


            result = diplomat_dao.insert_one(obj_diplomat)

            if result == 0:
                return "ERROR"

            return "Diplomat ADDED SUCCESSFULLY"

        except Exception as e:
            print(f'Error_DiplomatController.add_one_diplomat() ::: {e}')

        return None

    @staticmethod
    def modify_one_diplomat(diplomat_id, name,countryId):
        '''
        Modify a diplomat.
        @param diplomat_id: ID of the diplomat.
        @param name: New name of the diplomat.
        @param countryId: New name of the diplomat.
        @return: Status of modifying the diplomat.
        '''
        try:
            diplomat_dao = DiplomatDAO()
            obj_diplomat = Diplomat()
            c1 = Country()

            c1.setCountryId(countryId)

            obj_diplomat.set_Diplomatcountry(c1)
            obj_diplomat.setName(name)


            result = diplomat_dao.modify_one(diplomat_id, obj_diplomat)

            if result == 0:
                return "ERROR"

            return "Diplomat MODIFIED SUCCESSFULLY"

        except Exception as e:
            print(f'Error_DiplomatController.modify_one_diplomat() ::: {e}')

        return None

    @staticmethod
    def delete_one_diplomat(diplomat_id):
        '''
        Delete a treaty.
        @param diplomat_id: ID of the diplomat.
        @return: Status of deleting the diplomat.
        '''
        try:
            diplomat_dao = DiplomatDAO()
            result = diplomat_dao.delete_one(diplomat_id)

            if result == 0:
                return "ERROR"

            return "DIPLOMAT DELETED SUCCESSFULLY"

        except Exception as e:
            print(f'Error_DiplomatController.delete_one_diplomat() ::: {e}')

        return None

    @staticmethod
    def search_product_by_name(keyword) -> list[Diplomat]|str:
        """
        Rechercher des diplomat par nom.
        @param keyword: Mot-clé de recherche.
        @return: Liste des produits correspondant à la recherche au format JSON.
        """
        try:

            diplomatDAO = DiplomatDAO()

            listDiplomat: list[Diplomat] = diplomatDAO.searchPleinText(keyword)

            if listDiplomat == None:
                return "ERROR"

            return listDiplomat

        except Exception as e:

            print(f"Erreur_DiplomatC.search_product_by_name() ::: {e}")

        return None