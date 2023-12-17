from controller.SignatureC import SignatureController
from controller.CountryC import CountryController
from controller.TreatyC import TreatyController


#br = Brands()

liste_signatures = TreatyController.view_all_treaties()
print(liste_signatures)

listeS = []

print("##################################")

if liste_signatures is not None:
    for s in liste_signatures:
        idb = s.getTreatyId()
        nom = s.getName()
        print(idb, nom)
        listeS.append((idb, nom))
else:
    print("List of signatures is None.")
 # [], {}, (a,b)

print("**********************************")

print(listeS)
#%%
