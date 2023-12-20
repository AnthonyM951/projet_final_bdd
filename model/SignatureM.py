from datetime import date
from model.CountryM import Country
from model.TreatyM import Treaty
class Signature:
    def __init__(self):
        self.__signatureId: int = None
        self.__treatyId: Treaty 
        self.__countryOne: Country = None
        self.__countryTwo: Country = None
        self.__date: date = None
        self.__description: str = ""
        self.__status: str = ""


    def setSignatureId(self, signature: int) -> None:
        '''
        La méthode qui permet d'insérer une valeur dans l'attribut signatureId.

        :param signatureId: L'identifiant de la signature.
        :return: Rien.
        '''
        self.__signatureId = signature

    def getSignatureId(self) -> int:
        '''
        Cette méthode permet de retourner l'identifiant de la signature.

        :return: L'identifiant de la signature.
        '''
        return self.__signatureId
    
    def setTreatyId(self, treatyId: Treaty) -> None:
        '''
        La méthode qui permet d'insérer une valeur dans l'attribut treatyId.

        :param treatyId: L'ID du traité
        :return: Rien.
        '''
        self.__treatyId = treatyId

    def getTreatyId(self) -> Treaty:
        '''
        Cette méthode permet de retourner l'ID du traité.

        :return: L'ID du traité.
        '''
        return self.__treatyId

    def setCountryOne(self, countryOne: Country) -> None:
        '''
        La méthode qui permet d'insérer une valeur dans l'attribut countryFrom.

        :param countryOne: Le pays un partie de la signature.
        :return: Rien.
        '''
        self.__countryOne = countryOne

    def getCountryOne(self) -> Country:
        '''
        Cette méthode permet de retourner Le pays un partie de la signature.

        :return: Le pays un partie de la signature.
        '''
        return self.__countryOne

    def setCountryTwo(self, countryTwo: Country) -> None:
        '''
        La méthode qui permet d'insérer une valeur dans l'attribut countryTwo.

        :param countryTwo: Le pays deux partie de la signature.
        :return: Rien.
        '''
        self.__countryTwo = countryTwo

    def getCountryTwo(self) -> Country:
        '''
        Cette méthode permet de retourner le pays deux partie de la signature.

        :return: Le pays deux partie de la signature.
        '''
        return self.__countryTwo


    def setDate(self, date: date) -> None:
        '''
        La méthode qui permet d'insérer une valeur dans l'attribut year.

        :param year: L'année de signature.
        :return: Rien.
        '''
        self.__date = date

    def getDate(self) -> int:
        '''
        Cette méthode permet de retourner l'année de signature.

        :return: L'année de signature.
        '''
        return self.__date

    def setDescription(self, description: str) -> None:
        '''
        La méthode qui permet d'insérer une valeur dans l'attribut description.

        :param description: La description de la signature.
        :return: Rien.
        '''
        self.__description = description

    def getDescription(self) -> str:
        '''
        Cette méthode permet de retourner la description du flux de marchandises.

        :return: La description du flux de marchandises.
        '''
        return self.__description


    def setStatus(self, status : str) -> None:
        '''
        la méthode qui permet d'insérer une valeur dans l'attribut signatureId
        :param brandId: l'identifiant de la signature
        :return: rien
        '''
        self.__status = status
    def getStatus(self) -> str:
        '''
        cette méthode permet de retourner l'identifiant d'une signature
        :return: l'id d'une signature
        '''
        return self.__status

