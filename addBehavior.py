'''
Created on 25 Jan 2016

@author: craig
'''

class AddBehavior(object):
    '''
    -"default" behavior for adding Products
    -total cost is incremented but retail price is updated 
    -this allows for feedback on current unit retail cost (Latest) for an item
    '''

#default add behavior
    def addItem(self,prodct,count,cost,retail):

        prodct.count+=count
        prodct.totalCost+= cost * count 
        prodct.retail=retail #retail is not weighted only updated
        
        return prodct