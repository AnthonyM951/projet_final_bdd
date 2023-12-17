from dao import ModelDAO
from model.CountryM import Country

class CountryDAO(ModelDAO.modeleDAO):

    def __init__(self):
        '''
        Initialize the CountryDAO object by establishing a connection to the database.
        '''
        params = ModelDAO.modeleDAO.connect_object
        self.cur = params.cursor()

    def insert_one(self, obj_ins: Country) -> int:
        '''
        Insert an object into the Country table.

        :param obj_ins: The object to insert into the table.
        :return: The number of affected rows.
        '''
        try:
            query = '''INSERT INTO bdd_projet_final.country (country_id, country_name, capital, population, area) 
                       VALUES (%s, %s, %s, %s, %s);'''
            self.cur.execute(query, (obj_ins.getCountryId(), obj_ins.getCountry_name(), obj_ins.getCapital(),
                                     obj_ins.getPopulation(), obj_ins.getArea()))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Error_CountryDAO.insert_one() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def find_one(self, key_to_find) -> Country:
        '''
        Find an object in the Country table by key.

        :param key_to_find: The search key.
        :return: The found object.
        '''
        try:
            query = '''SELECT * FROM bdd_projet_final.country WHERE country_id = %s;'''
            self.cur.execute(query, (key_to_find,))
            res = self.cur.fetchone()

            if res:
                country = Country()
                country.setCountryId(res[0])
                country.setCountry_name(res[1])
                country.setCapital(res[2])
                country.setPopulation(res[3])
                country.setArea(res[4])

                return country
            else:
                return None
        except Exception as e:
            print(f"Error_CountryDAO.find_one() ::: {e}")
        finally:
            self.cur.close()

    def find_all(self) -> list[Country]:
        '''
        Retrieve all records from the Country table.

        :return: A list of Country objects.
        '''
        try:
            query = '''SELECT * FROM bdd_projet_final.country;'''
            self.cur.execute(query)
            res = self.cur.fetchall()

            country_list = []

            if len(res) > 0:
                for r in res:
                    country = Country()
                    country.setCountryId(r[0])
                    country.setCountry_name(r[1])
                    country.setCapital(r[2])
                    country.setPopulation(r[3])
                    country.setArea(r[4])

                    country_list.append(country)

                return country_list
            else:
                return None
        except Exception as e:
            print(f"Error_CountryDAO.find_all() ::: {e}")
        finally:
            self.cur.close()

    def modify_one(self, key_to_modify, obj_modify: Country) -> int:
        '''
        Modify a record in the Country table.

        :param key_to_modify: The key of the record to modify.
        :param obj_modify: The new data to update.
        :return: The number of affected rows.
        '''
        try:
            query = '''UPDATE bdd_projet_final.country SET 
                       country_name = %s, 
                       capital = %s, 
                       population = %s, 
                       area = %s 
                       WHERE country_id = %s;'''
            self.cur.execute(query, (obj_modify.getCountry_name(), obj_modify.getCapital(), obj_modify.getPopulation(),
                                     obj_modify.getArea(), key_to_modify))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Error_CountryDAO.modify_one() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def delete_one(self, key_to_delete) -> int:
        '''
        Delete a record from the Country table.

        :param key_to_delete: The key of the record to delete.
        :return: The number of affected rows.
        '''
        try:
            query = '''DELETE FROM bdd_projet_final.country WHERE country_id = %s;'''
            self.cur.execute(query, (key_to_delete,))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Error_CountryDAO.delete_one() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()
    def insererUn(self, objIns)->int:
        pass


    def insererToutList(self, objInsList)->int:
        pass

    # SELECT


    def trouverUn(self, cleTrouv)->object:
        pass

    def trouverTout(self)->list:
        pass

    
    def trouverToutParUn(self, cleTrouv)->list:
        pass

    
    def trouverToutParUnLike(self, cleTrouv)->list:
        pass

    # UPDATE

    
    def modifierUn(self, cleAnc, objModif)->int:
        pass

    # DELETE

    
    def supprimerUn(self, cleSup)->int:
        pass

    # SEANCE 4/5 :
    # 1.    La moyenne des dépenses effectuées par le client (PL/SQL)
    # 2.    CASE WHEN : filtrer par statut
    # 3.    RANK : classer les produits par prix croissant
    # 4.    @@ : faire une recherche plein texte

    
    def depensesMoyennes(self)->float:
        pass

    
    def filtrerCmdByStatus(self)->list:
        pass

    
    def sortProductByPrice(self)->list:
        pass

    
    def searchPleinText(self)->list:
        pass

    # SEANCE 6 :
    # 1.    User/Rôles
    # 2.    MD5 password
    # 3.    Indexation
    # 4.    Enum/DATE_TRUNC

    
    def creerUser(self, pwd, usr)->object:
        pass

    
    def creerRole(self, role)->int:
        pass

    
    def attribuerRole(self, usr,role)->int:
        pass

    # def get_countries_with_population_above(self, population_threshold):
    #     '''
    #     Get countries with a population above a specified threshold using PL/SQL function.
    #     @param population_threshold: The population threshold.
    #     @return: List of countries.
    #     '''
    #     try:
    #         query = '''BEGIN OPEN :result_cursor FOR get_countries_above_population_threshold(:population_threshold); END;'''
    #         cursor = self.cur.var(cx_Oracle.CURSOR)
    #         self.cur.execute(query, result_cursor=cursor, population_threshold=population_threshold)

    #         country_list = []

    #         for r in cursor:
    #             country = Country()
    #             country.set_country_id(r[0])
    #             country.set_country_name(r[1])
    #             country.set_capital(r[2])
    #             country.set_population(r[3])
    #             country.set_area(r[4])

    #             country_list.append(country)

    #         return country_list

    #     except Exception as e:
    #         print(f"Error_CountryDAO.get_countries_with_population_above() ::: {e}")
    #     finally:
    #         self.cur.close()
    # # Add other methods as needed
