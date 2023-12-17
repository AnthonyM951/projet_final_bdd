from dao import ModelDAO
from model.DiplomatM import Diplomat
from model.CountryM import Country

class DiplomatDAO(ModelDAO.ModelDAO):

    def __init__(self):
        '''
        Initialize the diplomatDAO object by establishing a connection to the database.
        '''
        params = ModelDAO.modeleDAO.connect_object
        self.cur = params.cursor()

    def insert_one(self, obj_ins: Diplomat) -> int:
        '''
        Insert an object into the diplomat table.

        :param obj_ins: The object to insert into the table.
        :return: The number of affected rows.
        '''
        try:
            sql = "INSERT INTO Diplomat (diplomatName, countryId) VALUES (%s, %s) RETURNING diplomatId;"
            data = (obj_ins.get_diplomat_name(), obj_ins.get_Diplomatcountry().getCountryId())

            with self.connection.cursor() as cursor:
                cursor.execute(sql, data)
                diplomat_id = cursor.fetchone()[0]
                self.connection.commit()

            return diplomat_id

        except Exception as e:
            print(f"Error in DiplomatDAO.insert_diplomat: {e}")
            return None

    def find_one(self, key_to_find) -> Diplomat:
        '''
        Find an object in the diplomat table by key.

        :param key_to_find: The search key.
        :return: The found object.
        '''
        try:
            query = '''SELECT * FROM bdd_projet_final.diplomat WHERE diplomat_id = %s;'''
            self.cur.execute(query, (key_to_find,))
            res = self.cur.fetchone()

            if res:
                diplomat = Diplomat()
                diplomat.set_diplomat_id(res[0]),
                diplomat.set_diplomat_name(res[1]),
                diplomat.set_Diplomatcountry(res[2])

                return diplomat
            else:
                return None
        except Exception as e:
            print(f"Error_diplomatDAO.find_one() ::: {e}")
        finally:
            self.cur.close()

    def find_all(self) -> list[Diplomat]:
        '''
        Retrieve all records from the diplomat table.

        :return: A list of diplomat objects.
        '''
        try:
            query = '''SELECT * FROM bdd_projet_final.diplomat;'''
            self.cur.execute(query)
            res = self.cur.fetchall()

            diplomat_list = []

            if len(res) > 0:
                for r in res:
                    diplomat = Diplomat()
                    diplomat.set_diplomat_id(r[0])
                    diplomat.set_diplomat_name(r[1])
                    diplomat.set_Diplomatcountry(r[1])

                    diplomat_list.append(diplomat)

                return diplomat_list
            else:
                return None
        except Exception as e:
            print(f"Error_diplomatDAO.find_all() ::: {e}")
        finally:
            self.cur.close()

    def modify_one(self, key_to_modify, obj_modify: Diplomat) -> int:
        '''
        Modify a record in the diplomat table.

        :param key_to_modify: The key of the record to modify.
        :param obj_modify: The new data to update.
        :return: The number of affected rows.
        '''
        try:
            query = '''UPDATE bdd_projet_final.diplomat SET 
                       diplomatName = %s,
                       countryId= %s
                       WHERE diplomat_id = %s;'''
            self.cur.execute(query, (obj_modify.get_diplomat_name(),obj_modify.get_Diplomatcountry().getCountryId(), key_to_modify))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Error_diplomatDAO.modify_one() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def delete_one(self, key_to_delete) -> int:
        '''
        Delete a record from the diplomat table.

        :param key_to_delete: The key of the record to delete.
        :return: The number of affected rows.
        '''
        try:
            query = '''DELETE FROM bdd_projet_final.diplomat WHERE diplomatId = %s;'''
            self.cur.execute(query, (key_to_delete,))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Error_diplomatDAO.delete_one() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    # def filter_by_year(self,year):
    #     '''
    #     Apply a filter to retrieve goods flows based on the provided status.

    #     :param status: The status to filter.
    #     :return: List of goods flows matching the given status.
    #     '''
    #     try:
    #         query = f'''
    #             SELECT * FROM bdd_projet_final.diplomat
    #             WHERE CASE WHEN status = '{year}' THEN 1 ELSE 0 END = 1;
    #         '''
    #         self.cur.execute(query)
    #         res = self.cur.fetchall()

    #         diplomat_list = []

    #         if len(res) > 0:
    #             for r in res:
    #                 diplomat = diplomat()
    #                 diplomat.setdiplomatId(r[0])
    #                 diplomat.setCountryFrom(r[1])
    #                 diplomat.set_country_to(r[2])
    #                 diplomat.set_value(r[3])
    #                 diplomat.set_year(r[4])
    #                 diplomat.set_description(r[5])
    #                 diplomat.set_status(r[6])

    #                 diplomat_list.append(diplomat)

    #             return diplomat_list
    #         else:
    #             return None
    #     except Exception as e:
    #         print(f"Error_diplomatDAO.filter_by_status() ::: {e}")
    #     finally:
    #         self.cur.close()
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

    # Add other methods as needed
