'''
Created on 24 Jan 2016

@author: craig
'''

import csv
from product import Product



class IFixList(dict):
    '''
    The interface for iFix subclasses
    '''
    
    
    def addProducts(self,path):
        #read csv
        with open(path, 'rb') as input:
            csvRead = csv.reader(input, delimiter= ',')
            headers=csvRead.next()
            pId = headers.index(self.idName)
            pCount=headers.index(self.idQ)
            pCost=headers.index(self.idCost)
            pPrice=headers.index(self.idPrice)
            
            
            #for row in csv, if key not in dict, add new product with key ProductID
            for row in csvRead:
                # defined for readability 
                productId=(row[pId]) 
                #check there is such a product in the inventory
#                 raise Exception
                productCount=int(float(row[pCount]))
                productCost=float(row[pCost])
                productPrice=float(row[pPrice])
                    
                if self.has_key(productId):
                    self[productId].addItem(productCount,productCost,productPrice)
                else:
                    newProduct=Product()
                    newProduct=newProduct.addItem(productCount,productCost,productPrice)
                    self[productId] = newProduct