from dao.TreatyDAO import TreatyDAO
from model.TreatyM import Treaty

class TreatyController:

    @staticmethod
    def view_all_treaties():
        '''
        View all treaties.
        @return: List of treaties.
        '''
        try:
            treaty_dao = TreatyDAO()
            treaties = treaty_dao.find_all()

            if treaties is None:
                return "ERROR"

            return treaties

        except Exception as e:
            print(f'Error_TreatyController.view_all_treaties() ::: {e}')

        return None

    @staticmethod
    def view_one_treaty(treaty_id):
        '''
        View a specific treaty.
        @param treaty_id: ID of the treaty.
        @return: Specific treaty.
        '''
        try:
            treaty_dao = TreatyDAO()
            treaty = treaty_dao.find_one(treaty_id)

            if treaty is None:
                return "ERROR"

            return treaty

        except Exception as e:
            print(f'Error_TreatyController.view_one_treaty() ::: {e}')

        return None

    @staticmethod
    def add_one_treaty(treaty_id, name):
        '''
        Add a treaty.
        @param treaty_id: ID of the treaty.
        @param name: Name of the treaty.
        '''
        try:
            treaty_dao = TreatyDAO()
            obj_treaty = Treaty()

            obj_treaty.setTreatyId(treaty_id)
            obj_treaty.setName(name)


            result = treaty_dao.insert_one(obj_treaty)

            if result == 0:
                return "ERROR"

            return "TREATY ADDED SUCCESSFULLY"

        except Exception as e:
            print(f'Error_TreatyController.add_one_treaty() ::: {e}')

        return None

    @staticmethod
    def modify_one_treaty(treaty_id, name):
        '''
        Modify a treaty.
        @param treaty_id: ID of the treaty.
        @param name: New name of the treaty.
        @return: Status of modifying the treaty.
        '''
        try:
            treaty_dao = TreatyDAO()
            obj_treaty = Treaty()

            obj_treaty.setName(name)


            result = treaty_dao.modify_one(treaty_id, obj_treaty)

            if result == 0:
                return "ERROR"

            return "TREATY MODIFIED SUCCESSFULLY"

        except Exception as e:
            print(f'Error_TreatyController.modify_one_treaty() ::: {e}')

        return None

    @staticmethod
    def delete_one_treaty(treaty_id):
        '''
        Delete a treaty.
        @param treaty_id: ID of the treaty.
        @return: Status of deleting the treaty.
        '''
        try:
            treaty_dao = TreatyDAO()
            result = treaty_dao.delete_one(treaty_id)

            if result == 0:
                return "ERROR"

            return "TREATY DELETED SUCCESSFULLY"

        except Exception as e:
            print(f'Error_TreatyController.delete_one_treaty() ::: {e}')

        return None
