'''
Created on 25 Jan 2016

@author: craig
'''
from addBehavior import AddBehavior

class SalesAddBehavior(AddBehavior):
    '''
    -Interface for specific add behavior
    -The retail amount is incremented to a total for all sales
    -Objects implementing this do not require feedback on retail price per item
    -This behavior can be applied to any number of IFixList children
    '''

    def addItem(self, prodct, count, cost, retail):
        
        prodct.count+=count
        prodct.totalCost+= (cost * count) 
        prodct.retail+= (retail*count)                           
        
        return prodct