from model.CountryM import Country

class Diplomat:
    def __init__(self):
        self.__diplomat_id: int = None
        self.__diplomat_name: str = None
        self.__country_id: Country = None
        

    def set_diplomat_id(self, diplomat_id):
        self.__diplomat_id = diplomat_id

    def get_diplomat_id(self):
        return self.__diplomat_id

    def set_diplomat_name(self, diplomat_name):
        self.__diplomat_name = diplomat_name

    def get_diplomat_name(self):
        return self.__diplomat_name

    def set_Diplomatcountry(self, country_id:Country):
        self.__country_id = country_id

    def get_Diplomatcountry(self):
        return self.__country_id