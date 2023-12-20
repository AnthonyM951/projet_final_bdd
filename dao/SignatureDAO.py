from dao import ModelDAO
from model.SignatureM import Signature
from model.CountryM import Country

class SignatureDAO(ModelDAO.modeleDAO):

    def __init__(self):
        '''
        Initialize the SignatureDAO object by establishing a connection to the database.
        '''
        params = ModelDAO.modeleDAO.connect_object
        self.cur = params.cursor()

    def insert_one(self, obj_ins: Signature) -> int:
        '''
        Insert an object into the Signature table.

        :param obj_ins: The object to insert into the table.
        :return: The number of affected rows.
        '''
        try:
            query = '''INSERT INTO bdd_projet_final.signature (signature_id, treatyId, countryOne, countryTwo, date_, description,status) 
                       VALUES (%s,%s, %s, %s, %s, %s,%s);'''
            self.cur.execute(query, (obj_ins.getSignatureId(), obj_ins.getTreatyId().getTreatyId(), obj_ins.getCountryOne().getCountryId(), obj_ins.getCountryTwo().getCountryId(),
                                     obj_ins.getDate(), obj_ins.getDescription(),obj_ins.getStatus))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Error_SignatureDAO.insert_one() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def find_one(self, key_to_find) -> Signature:
        '''
        Find an object in the signature table by key.

        :param key_to_find: The search key.
        :return: The found object.
        '''
        try:
            query = '''SELECT * FROM bdd_projet_final.signature WHERE signature_id = %s;'''
            self.cur.execute(query, (key_to_find,))
            res = self.cur.fetchone()

            if res:
                signature = Signature()
                signature.setSignatureId(res[0])
                signature.setTreatyId(res[1])
                signature.setCountryOne(res[2])
                signature.setCountryTwo(res[3])
                signature.setDate(res[4])
                signature.setDescription(res[5])
                signature.setStatus(res[6])

                return signature
            else:
                return None
        except Exception as e:
            print(f"Error_SignatureDAO.find_one() ::: {e}")
        finally:
            self.cur.close()

    def find_all(self) -> list[Signature]:
        '''
        Retrieve all records from the Signature table.

        :return: A list of Signature objects.
        '''
        try:
            query = '''SELECT * FROM  bdd_projet_final.signature;'''
            self.cur.execute(query)
            res = self.cur.fetchall()

            signature_list = []

            if len(res) > 0:
                for r in res:
                    signature = Signature()
                    signature.setSignatureId(res[0])
                    signature.setTreatyId(res[1])
                    signature.setCountryOne(res[2])
                    signature.setCountryTwo(res[3])
                    signature.setDate(res[4])
                    signature.setDescription(res[5])
                    signature.setStatus(res[6])

                    signature_list.append(signature)

                return signature_list
            else:
                return None
        except Exception as e:
            print(f"Error_SignatureDAO.find_all() ::: {e}")
        finally:
            self.cur.close()

    def modify_one(self, key_to_modify, obj_modify: Signature) -> int:
        '''
        Modify a record in the Signature table.

        :param key_to_modify: The key of the record to modify.
        :param obj_modify: The new data to update.
        :return: The number of affected rows.
        '''
        try:
            query = '''UPDATE bdd_projet_final.signature SET 
                       treatyId= %s,
                       country_from = %s, 
                       country_to = %s, 
                       date_ = %s, 
                       description = %s,
                       status= %s, 
                       WHERE signature_id = %s;'''
            self.cur.execute(query, (obj_modify.getTreatyId().getTreatyId(),obj_modify.getCountryOne().getCountryId(), obj_modify.getCountryTwo().getCountryId(),
                                     obj_modify.getDate(), obj_modify.getDescription(),obj_modify.getStatus(), key_to_modify))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Error_SignatureDAO.modify_one() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def delete_one(self, key_to_delete) -> int:
        '''
        Delete a record from the Signature table.

        :param key_to_delete: The key of the record to delete.
        :return: The number of affected rows.
        '''
        try:
            query = '''DELETE FROM bdd_projet_final.signature WHERE signature_id = %s;'''
            self.cur.execute(query, (key_to_delete,))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Error_SignatureDAO.delete_one() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def sortSignatureByDate(self) -> list[Signature]:
        '''
        Trie les signatures par date.

        :return: Une liste de signatures triées.
        '''
        try:
            query = '''SELECT treatyId, countryOne, countryTwo, date_, description, status, RANK() OVER (ORDER BY date_)
                        FROM bdd_projet_final.signature;'''
            self.cur.execute(query)
            res = self.cur.fetchall()

            liste_signatures = []

            if len(res) > 0:
                for r in res:
                    signature = Signature()
                    signature.setTreatyId(r[0])
                    signature.setCountryOne(r[1])
                    signature.setCountryTwo(r[2])
                    signature.setDate(r[3])
                    signature.setDescription(r[4])
                    signature.setStatus(r[5])
                    signature.setSignatureId(r[6])
                    liste_signatures.append(signature)

                return liste_signatures

            else:
                return None

        except Exception as e:
            print(f"Erreur_SignatureDAO.sortSignatureByDate() ::: {e}")
        finally:
            self.cur.close()
    def get_status_by_signature(self, signature_id: int) -> str | None:
        """
        Get the status by signature.
        @param signature_id: Signature ID.
        @return: Status of the signature.
        """
        try:
            query = f'SELECT status FROM bdd_projet_final.signature WHERE signatureid = {signature_id};'
            self.cur.execute(query)
            result = self.cur.fetchone()

            if result:
                return result[0]  # Assuming status is in the first column

            return None

        except Exception as e:
            print(f"Error_SignatureDAO.get_status_by_signature() ::: {e}")
            return None
    # Add other methods as needed


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
