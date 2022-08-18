class Dictordonne():

    def __init__(self,**dicto):
        self.DicElement = dicto
        self.listCle=[]
        self.listValeur=[]
        for cle in self.DicElement.keys():
            self.listCle.append(cle)
        for valeur in self.DicElement.values():
            self.listValeur.append(valeur)

        self.position = len(self.listCle)    
    
    def __setitem__(self, cles, valeur):
        if (cles in self.listCle) == False: #if the key don't stand in the keylist, the loop will carry out
            self.listCle.append(cles)
            self.listValeur.append(valeur)
        else:                               #if the key already exist, therefore one modified its value
            ind = self.listCle.index(cles)
            self.listValeur[ind] = valeur
        
        self.DicElement[cles] = valeur  #the Dictionary of Elemente will be anyway modify  

    def __delitem__(self, key):
        ind = self.listCle.index(key)
        del self.listCle[ind]
        del self.listValeur[ind]
        del self.DicElement[key]

    def __getitem__(self, key):
        return self.DicElement[key]

    def keys(self):
        return self.listCle
    
    def values(self):
        return self.listValeur
    
    def __contains__(self, key):
        return key in self.listCle

    def sort(self):
        self.listCle.sort()
        self.listValeur=list()
        for key in self.listCle:
            self.listValeur.append(self.DicElement[key])
        
        self.DicElement = dict()
        listFictiv = list(self.listValeur)
        for key in  self.listCle:
            #listFictiv = list(self.listValeur)
            for valeur in listFictiv:
                self.DicElement[key] = valeur
                del listFictiv[0]
                break
    def reverse(self):
        self.listCle.reverse()
        self.listValeur.reverse()
        self.DicElement = dict()
        listFictiv = list(self.listValeur)
        for key in  self.listCle:
            #listFictiv = list(self.listValeur)
            for valeur in listFictiv:
                self.DicElement[key] = valeur
                del listFictiv[0]
                break
    
    def items(self):
        listTubleElt = list()
        for key, values in self.DicElement.items():
            listTubleElt.append((key, values))
        return listTubleElt   
    
    def __add__(self, newDict):
        for key, values  in newDict.items():
            self.DicElement[key] = values
            self.listCle.append(key)
            self.listValeur.append(values)
    
    def __iter__(self):
        return iter(self.listCle) 
    
    #def __next__(self):
    #   n = 0
    #    if n == self.position:
    #        raise StopIteration
    #    n = n+1
    #    return self.listCle[n-1]
            

    def __str__(self):
        return "{}{}{}".format(self.DicElement, self.listCle, self.listValeur)    

