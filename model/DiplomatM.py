from model.CountryM import Country

class Diplomat:
    def __init__(self):
        self.__diplomat_id: int = None
        self.__diplomat_name: str = None
        self.__country_id: Country = None
        

    def setDiplomatId(self, diplomatId):
        '''
        Méthode pour définir l'identifiant du diplomate.
        :param diplomatId: L'identifiant du diplomate.
        :return: Aucun.
        '''
        self.__diplomat_id = diplomatId

    def getDiplomatId(self):
        '''
        Méthode pour obtenir l'identifiant du diplomate.
        :return: L'identifiant du diplomate.
        '''
        return self.__diplomat_id

    def setDiplomatName(self, diplomatName):
        '''
        Méthode pour définir le nom du diplomate.
        :param diplomatName: Le nom du diplomate.
        :return: Aucun.
        '''
        self.__diplomat_name = diplomatName

    def getDiplomatName(self):
        '''
        Méthode pour obtenir le nom du diplomate.
        :return: Le nom du diplomate.
        '''
        return self.__diplomat_name

    def setDiplomatCountry(self, countryId: Country):
        '''
        Méthode pour définir le pays du diplomate.
        :param countryId: Objet de type Country représentant le pays du diplomate.
        :return: Aucun.
        '''
        self.__country_id = countryId

    def getDiplomatCountry(self):
        '''
        Méthode pour obtenir le pays du diplomate.
        :return: Objet de type Country représentant le pays du diplomate.
        '''
        return self.__country_id
