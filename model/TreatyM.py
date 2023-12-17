from datetime import datetime
from model.CountryM import Country

class Treaty :
    def __init__(self):
        self.__treatyId: int = None
        self.__name: str = ""
        

    def setTreatyId(self, treatyId : int) -> None:
        '''
        la méthode qui permet d'insérer une valeur dans l'attribut brandId
        :param brandId: l'identifiant de la marque
        :return: rien
        '''
        self.__treatyId = treatyId
    def getTreatyId(self) -> int:
        '''
        cette méthode permet de retourner l'identifiant d'une marque
        :return: l'id d'une marque
        '''
        return self.__treatyId

    def setName(self, name : int) -> None:
        '''
        la méthode qui permet d'insérer une valeur dans l'attribut brandId
        :param brandId: l'identifiant de la marque
        :return: rien
        '''
        self.__name = name
    def getName(self) -> str:
        '''
        cette méthode permet de retourner l'identifiant d'une marque
        :return: l'id d'une marque
        '''
        return self.__name

    def setDate(self, date : datetime) -> None:
        '''
        la méthode qui permet d'insérer une valeur dans l'attribut brandId
        :param brandId: l'identifiant de la marque
        :return: rien
        '''
        self.__date = date
    def getDate(self) -> datetime:
        '''
        cette méthode permet de retourner l'identifiant d'une marque
        :return: l'id d'une marque
        '''
        return self.__date

    def setparticipantOne(self, participantOne : Country) -> None:
        '''
        la méthode qui permet d'insérer une valeur dans l'attribut brandId
        :param participantOne: l'identifiant du participantOne
        :return: rien
        '''
        self.__participantOne = participantOne
    def getparticipantOne(self) -> Country:
        '''
        cette méthode permet de retourner l'identifiant d'une marque
        :return: l'id d'une marque
        '''
        return self.__participantOne
    
    def setparticipantTwo(self, participantTwo : Country) -> None:
        '''
        la méthode qui permet d'insérer une valeur dans l'attribut participantTwo
        :param participantTwo: l'identifiant du participantTwo
        :return: rien
        '''
        self.__participantTwo = participantTwo
    def getparticipantTwo(self) -> Country:
        '''
        cette méthode permet de retourner l'identifiant du participantTwo
        :return: l'id du participantTwo
        '''
        return self.__participantTwo

    def setDescription(self, description : str) -> None:
        '''
        la méthode qui permet d'insérer une valeur dans l'attribut brandId
        :param brandId: l'identifiant de la marque
        :return: rien
        '''
        self.__description = description
    def getDescription(self) -> str:
        '''
        cette méthode permet de retourner l'identifiant d'une marque
        :return: l'id d'une marque
        '''
        return self.__description

