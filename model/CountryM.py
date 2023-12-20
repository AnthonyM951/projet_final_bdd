class Country :
    def __init__(self):
        self.__country_id: int = None
        self.__country_name: str=""
        self.__capital: str=""
        self.__population: int = None
        self.__area: int = None

    def setCountryId(self, countryId: int) -> None:
        '''
        La méthode qui permet d'insérer une valeur dans l'attribut countryId.
        :param countryId: l'identifiant du pays.
        :return: rien
        '''
        self.__country_id = countryId

    def getCountryId(self) -> int:
        '''
        Cette méthode permet de retourner l'identifiant d'un pays.
        :return: l'id d'un pays.
        '''
        return self.__country_id

    def setCountryName(self, countryName: str) -> None:
        '''
        La méthode qui permet d'insérer une valeur dans l'attribut countryName.
        :param countryName: le nom du pays.
        :return: rien
        '''
        self.__country_name = countryName

    def getCountryName(self) -> str:
        '''
        Cette méthode permet de retourner le nom du pays.
        :return: le nom du pays.
        '''
        return self.__country_name

    def setCapital(self, capital: str) -> None:
        '''
        La méthode qui permet d'insérer une valeur dans l'attribut capital.
        :param capital: le nom de la capitale.
        :return: rien
        '''
        self.__capital = capital

    def getCapital(self) -> str:
        '''
        Cette méthode permet de retourner le nom de la capitale.
        :return: le nom de la capitale.
        '''
        return self.__capital

    def setPopulation(self, population: int) -> None:
        '''
        La méthode qui permet d'insérer une valeur dans l'attribut population.
        :param population: la population du pays.
        :return: rien
        '''
        self.__population = population

    def getPopulation(self) -> int:
        '''
        Cette méthode permet de retourner la population du pays.
        :return: la population du pays.
        '''
        return self.__population

    def setArea(self, area: int) -> None:
        '''
        La méthode qui permet d'insérer une valeur dans l'attribut area.
        :param area: la superficie du pays.
        :return: rien
        '''
        self.__area = area

    def getArea(self) -> int:
        '''
        Cette méthode permet de retourner la superficie du pays.
        :return: la superficie du pays.
        '''
        return self.__area