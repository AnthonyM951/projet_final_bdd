from dao.CountryDAO import CountryDAO
from model.CountryM import Country

class CountryController:

    @staticmethod
    def view_all_countries():
        '''
        View all countries.
        @return: List of countries.
        '''
        try:
            country_dao = CountryDAO()
            countries = country_dao.find_all()

            if countries is None:
                return "ERROR"

            return countries

        except Exception as e:
            print(f'Error_CountryController.view_all_countries() ::: {e}')

        return None

    @staticmethod
    def view_one_country(country_id):
        '''
        View a specific country.
        @param country_id: ID of the country.
        @return: Specific country.
        '''
        try:
            country_dao = CountryDAO()
            country = country_dao.find_one(country_id)

            if country is None:
                return "ERROR"

            return country

        except Exception as e:
            print(f'Error_CountryController.view_one_country() ::: {e}')

        return None

    @staticmethod
    def add_one_country(country_id, country_name, capital, population, area):
        '''
        Add a country.
        @param country_id: ID of the country.
        @param country_name: Name of the country.
        @param capital: Capital of the country.
        @param population: Population of the country.
        @param area: Area of the country.
        @return: Status of adding the country.
        '''
        try:
            country_dao = CountryDAO()
            obj_country = Country()

            obj_country.setCountryId(country_id)
            obj_country.setCountry_name(country_name)
            obj_country.setCapital(capital)
            obj_country.setPopulation(population)
            obj_country.setArea(area)

            result = country_dao.insert_one(obj_country)

            if result == 0:
                return "ERROR"

            return "COUNTRY ADDED SUCCESSFULLY"

        except Exception as e:
            print(f'Error_CountryController.add_one_country() ::: {e}')

        return None

    @staticmethod
    def modify_one_country(country_id, country_name, capital, population, area):
        '''
        Modify a country.
        @param country_id: ID of the country.
        @param country_name: New name of the country.
        @param capital: New capital of the country.
        @param population: New population of the country.
        @param area: New area of the country.
        @return: Status of modifying the country.
        '''
        try:
            country_dao = CountryDAO()
            obj_country = Country()

            obj_country.setCountry_name(country_name)
            obj_country.setCapital(capital)
            obj_country.setPopulation(population)
            obj_country.setArea(area)

            result = country_dao.modify_one(country_id, obj_country)

            if result == 0:
                return "ERROR"

            return "COUNTRY MODIFIED SUCCESSFULLY"

        except Exception as e:
            print(f'Error_CountryController.modify_one_country() ::: {e}')

        return None

    @staticmethod
    def delete_one_country(country_id):
        '''
        Delete a country.
        @param country_id: ID of the country.
        @return: Status of deleting the country.
        '''
        try:
            country_dao = CountryDAO()
            result = country_dao.delete_one(country_id)

            if result == 0:
                return "ERROR"

            return "COUNTRY DELETED SUCCESSFULLY"

        except Exception as e:
            print(f'Error_CountryController.delete_one_country() ::: {e}')

        return None

