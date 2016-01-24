'''
Created on 24 Jan 2016

@author: craig
'''
from iFixList import IFixList


class OrdersList(IFixList):
    '''
    classdocs
    '''
    def __init__(self ):

        self.idName="ProductId"
        self.idQ="Quantity"
        self.idCost="UnitCost"
        self.idPrice="UnitPrice"