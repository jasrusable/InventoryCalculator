'''
Created on 24 Jan 2016

@author: craig
'''

import csv
from product import Product
from iFixList import IFixList



class StoreInventory(IFixList):
    '''
    classdocs
    '''
    def __init__(self ):

        self.idName="ProductId"
        self.idQ="InventoryCount"
        self.idCost="Cost"
        self.idPrice="Price"