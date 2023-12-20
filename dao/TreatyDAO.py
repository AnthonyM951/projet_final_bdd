from dao import ModelDAO
from model.TreatyM import Treaty

class TreatyDAO(ModelDAO.modeleDAO):

    def __init__(self):
        '''
        Initialize the TreatyDAO object by establishing a connection to the database.
        '''
        params = ModelDAO.modeleDAO.connect_object
        self.cur = params.cursor()

    def insert_one(self, obj_ins: Treaty) -> int:
        '''
        Insert an object into the Treaty table.

        :param obj_ins: The object to insert into the table.
        :return: The number of affected rows.
        '''
        try:
            query = '''INSERT INTO bdd_projet_final.treaty (name) 
                       VALUES ( %s);'''
            self.cur.execute(query, (obj_ins.getName()))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Error_TreatyDAO.insert_one() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def find_one(self, key_to_find) -> Treaty:
        '''
        Find an object in the Treaty table by key.

        :param key_to_find: The search key.
        :return: The found object.
        '''
        try:
            query = '''SELECT * FROM bdd_projet_final.treaty WHERE treaty_id = %s;'''
            self.cur.execute(query, (key_to_find,))
            res = self.cur.fetchone()

            if res:
                treaty = Treaty()
                treaty.setTreatyId(res[0])
                treaty.setName(res[1])


                return treaty
            else:
                return None
        except Exception as e:
            print(f"Error_TreatyDAO.find_one() ::: {e}")
        finally:
            self.cur.close()

    def find_all(self) -> list[Treaty]:
        '''
        Retrieve all records from the Treaty table.

        :return: A list of Treaty objects.
        '''
        try:
            query = '''SELECT * FROM bdd_projet_final.treaty;'''
            self.cur.execute(query)
            res = self.cur.fetchall()

            treaty_list = []

            if len(res) > 0:
                for r in res:
                    treaty = Treaty()
                    treaty.setTreatyId(r[0])
                    treaty.setName(r[1])

                    treaty_list.append(treaty)

                return treaty_list
            else:
                return None
        except Exception as e:
            print(f"Error_TreatyDAO.find_all() ::: {e}")
        finally:
            self.cur.close()

    def modify_one(self, key_to_modify, obj_modify: Treaty) -> int:
        '''
        Modify a record in the Treaty table.

        :param key_to_modify: The key of the record to modify.
        :param obj_modify: The new data to update.
        :return: The number of affected rows.
        '''
        try:
            query = '''UPDATE bdd_projet_final.treaty SET 
                       name = %s 
                       WHERE treaty_id = %s;'''
            self.cur.execute(query, (obj_modify.getName(), key_to_modify))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Error_TreatyDAO.modify_one() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def delete_one(self, key_to_delete) -> int:
        '''
        Delete a record from the Treaty table.

        :param key_to_delete: The key of the record to delete.
        :return: The number of affected rows.
        '''
        try:
            query = '''DELETE FROM bdd_projet_final.treaty WHERE treaty_id = %s;'''
            self.cur.execute(query, (key_to_delete,))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Error_TreatyDAO.delete_one() ::: {e}")
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
    #             SELECT * FROM bdd_projet_final.treaty
    #             WHERE CASE WHEN status = '{year}' THEN 1 ELSE 0 END = 1;
    #         '''
    #         self.cur.execute(query)
    #         res = self.cur.fetchall()

    #         treaty_list = []

    #         if len(res) > 0:
    #             for r in res:
    #                 treaty = Treaty()
    #                 treaty.setTreatyId(r[0])
    #                 treaty.setCountryFrom(r[1])
    #                 treaty.set_country_to(r[2])
    #                 treaty.set_value(r[3])
    #                 treaty.set_year(r[4])
    #                 treaty.set_description(r[5])
    #                 treaty.set_status(r[6])

    #                 treaty_list.append(treaty)

    #             return treaty_list
    #         else:
    #             return None
    #     except Exception as e:
    #         print(f"Error_TreatyDAO.filter_by_status() ::: {e}")
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
