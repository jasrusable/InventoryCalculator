'''
Created on 24 Jan 2016

@author: Craig
'''


class Product(object):
    '''
    Object representing the basic product
    '''


    def __init__(self ):
        self.count= 0
        self.cost=  0
        self.retail=0
    
    def addItem(self,count,cost,retail):

        self.count+=count
        self.cost+= cost
        self.retail=retail #retail is not weighted only updated
        
        return self