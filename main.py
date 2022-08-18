from ClassPackage.Classe import Dictordonne
DicFruits = Dictordonne(orange = 2, bannane = 5, pamplemouse = -3, avocat = 1 )
print(DicFruits)
del DicFruits["orange"]
print(DicFruits)
print(DicFruits["bannane"])
DicFruits["pamplemouse"]=10
print(DicFruits)
print("bannane" in DicFruits)
DicFruits.sort()
print(DicFruits)
DicFruits.reverse()
print(DicFruits)
DicMaison = Dictordonne(salon=2, cuisine=3, chambre=10)
DicFruits+DicMaison
print(DicFruits)
for i in DicFruits:
    print(i)

print(DicFruits.values())
