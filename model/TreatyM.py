from datetime import datetime
from model.CountryM import Country

class Treaty :
    def __init__(self):
        self.__treatyId: int = None
        self.__name: str = ""
        

    def setTreatyId(self, treatyId: int) -> None:
        '''
        Méthode pour définir l'identifiant du traité.
        :param treatyId: L'identifiant du traité.
        :return: Aucun.
        '''
        self.__treatyId = treatyId

    def getTreatyId(self) -> int:
        '''
        Méthode pour obtenir l'identifiant du traité.
        :return: L'identifiant du traité.
        '''
        return self.__treatyId

    def setName(self, name: str) -> None:
        '''
        Méthode pour définir le nom du traité.
        :param name: Le nom du traité.
        :return: Aucun.
        '''
        self.__name = name

    def getName(self) -> str:
        '''
        Méthode pour obtenir le nom du traité.
        :return: Le nom du traité.
        '''
        return self.__name

    def setDate(self, date: datetime) -> None:
        '''
        Méthode pour définir la date du traité.
        :param date: La date du traité.
        :return: Aucun.
        '''
        self.__date = date

    def getDate(self) -> datetime:
        '''
        Méthode pour obtenir la date du traité.
        :return: La date du traité.
        '''
        return self.__date

    def setParticipantOne(self, participantOne: Country) -> None:
        '''
        Méthode pour définir le participant One du traité.
        :param participantOne: Objet de type Country représentant le participant One.
        :return: Aucun.
        '''
        self.__participantOne = participantOne

    def getParticipantOne(self) -> Country:
        '''
        Méthode pour obtenir le participant One du traité.
        :return: Objet de type Country représentant le participant One.
        '''
        return self.__participantOne

    def setParticipantTwo(self, participantTwo: Country) -> None:
        '''
        Méthode pour définir le participant Two du traité.
        :param participantTwo: Objet de type Country représentant le participant Two.
        :return: Aucun.
        '''
        self.__participantTwo = participantTwo

    def getParticipantTwo(self) -> Country:
        '''
        Méthode pour obtenir le participant Two du traité.
        :return: Objet de type Country représentant le participant Two.
        '''
        return self.__participantTwo

    def setDescription(self, description: str) -> None:
        '''
        Méthode pour définir la description du traité.
        :param description: La description du traité.
        :return: Aucun.
        '''
        self.__description = description

    def getDescription(self) -> str:
        '''
        Méthode pour obtenir la description du traité.
        :return: La description du traité.
        '''
        return self.__description


