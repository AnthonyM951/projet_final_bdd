from dao.SignatureDAO import SignatureDAO
from model.SignatureM import Signature
from model.CountryM import Country
from model.TreatyM import Treaty

class SignatureController:
    
    @staticmethod
    def view_all_signatures():
        '''
        View all signatures.
        @return: List of signatures.
        '''
        try:
            signature_dao = SignatureDAO()
            signatures: list[Signature] = signature_dao.find_all()


            if signatures is None:
                return "ERROR"

            return signatures

        except Exception as e:
            print(f'Error_SignaturesController.view_all_signatures() ::: {e}')

        return None

    @staticmethod
    def view_one_signature(signature_id):
        '''
        View a specific goods flow.
        @param goods_flow_id: ID of the goods flow.
        @return: Specific goods flow.
        '''
        try:
            signature_dao = SignatureDAO()
            signature = signature_dao.find_one(signature_id)

            if signature is None:
                return "ERROR"

            return signature

        except Exception as e:
            print(f'Error_StatusController.view_one_signature() ::: {e}')

        return None

    @staticmethod
    def add_one_signature(treaty_id, countryOne, countryTwo, date, description,status):
        '''
        Add a signature.
        @param signature_id: ID of the signature.
        @param treaty_id: ID of the treaty.
        @param countryOne: Country One to sign.
        @param countryTwo: Country two to sign.
        @param date: Country two to sign.
        @param description: Description of signature.
        @param status: Status of signature.
        @return: Status of adding the signature.
        '''
        try:
            signature_dao = SignatureDAO()
            obj_signature = Signature()

            treaty=Treaty()
            treaty.setTreatyId(treaty_id)
            obj_signature.setTreatyId(treaty)


            c1 = Country()
            c2 = Country()

            c1.setCountryId(countryOne)
            c2.setCountryId(countryTwo)

            obj_signature.setCountryOne(c1)
            obj_signature.setCountryTwo(c2)


            obj_signature.setDate(date)
            obj_signature.setDescription(description)
            obj_signature.setStatus(status)

            result = signature_dao.insert_one(obj_signature)

            if result == 0:
                return "ERROR"

            return "Signature ADDED SUCCESSFULLY"

        except Exception as e:
            print(f'Error_SignatureController.add_signature() ::: {e}')

        return None

    @staticmethod
    def modify_one_signature(signature_id,treatyId, countryOne, countryTwo, date, description,status):
        '''
        Modify a goods flow.
        @param signature_id: ID of the signature.
        @param treatyId: ID of the treaty.
        @param countryOne: First country to sign.
        @param countryTwo: Second country to sign.
        @param date: New date of signature.
        @param description: New description of signature.
        @param status: New status of signature.
        @return: Status of modifying the signature.
        '''
        try:
            signature_dao = SignatureDAO()
            obj_signature = Signature()
            treaty=Treaty()
            treaty.setTreatyId(treatyId)
            c1 = Country()
            c2 = Country()

            c1.setCountryId(countryOne)
            c2.setCountryId(countryTwo)

            obj_signature.setCountryOne(c1)
            obj_signature.setCountryTwo(c2)
            obj_signature.setDate(date)
            obj_signature.setDescription(description)
            obj_signature.setStatus(status)

            result = signature_dao.modify_one(signature_id, obj_signature)

            if result == 0:
                return "ERROR"

            return "Signature MODIFIED SUCCESSFULLY"

        except Exception as e:
            print(f'Error_SignatureController.modify_one_signature() ::: {e}')

        return None

    @staticmethod
    def delete_one_signature(signature_id):
        '''
        Delete a signature.
        @param signature_id: ID of the signature.
        @return: Status of deleting the signature.
        '''
        try:
            signature_dao = SignatureDAO()
            result = signature_dao.delete_one(signature_id)

            if result == 0:
                return "ERROR"

            return "Signature DELETED SUCCESSFULLY"

        except Exception as e:
            print(f'Error_SignatureController.delete_one_signature() ::: {e}')

        return None
    @staticmethod
    def sortSignatureByDate() -> list[Signature] | str:
        """
        Trier les signatures par date.
        @return: Liste des signatures triées au format JSON.
        """
        try:
            signature_dao = SignatureDAO()
            list_signatures: list[Signature] = signature_dao.sortSignatureByDate()

            if list_signatures is None:
                return "ERROR"

            return list_signatures

        except Exception as e:
            print(f"Erreur_SignatureController.sortSignatureByDate() ::: {e}")

        return None
    
    @staticmethod
    def get_status_by_signature(signature_id: int) -> str | None:
        """
        Get the status by signature.
        @param signature_id: Signature ID.
        @return: Status of the signature.
        """
        try:
            signature_dao = SignatureDAO()
            status: str | None = signature_dao.get_status_by_signature(signature_id)

            return status

        except Exception as e:
            print(f'Error_SignatureController.get_status_by_signature() ::: {e}')
            return None
