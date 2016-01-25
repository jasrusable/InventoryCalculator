'''
Created on 24 Jan 2016

@author: Craig
'''
import csv

from iFixList import IFixList
from salesAddBehaviour import SalesAddBehavior


class SalesProductList(IFixList):
    '''
    classdocs
    '''
    
    def __init__(self ):

        self.idName="ProductId"
        self.idQ="Quantity"
        self.idCost="UnitCost"
        self.idPrice="UnitPrice"
        self.addStyle=SalesAddBehavior()







        