'''
Created on 24 Jan 2016

@author: Craig
'''

class IFixStoreCalculator(object):
    '''
    This class is used as a calculator for iFix for various order, sales and inventory related calculations.
    
    '''
    

    def __init__(self, sales = {} , orders = {} , stock = {}):
        '''
        
        '''
        self.sales = sales
        self.orders= orders
        self.stock= stock
        
        
        
    def addNewInventory(self,path = "./Inventory.csv"):
        '''
        This function adds an Inventory list to an empty store
        '''
        #iterate through the Inventory and add Products to the stock dictionary
        
        return
    
    def addNewOrderList(self, path = " ./Orders.csv"):
        '''
        
        '''
        #iterate through the orders list and populate the orders dict (this is the orders object) with Products
        #check that the key exists in the Inventory
        #if not, add a new Inventory product with the new key
        #else add the 
        return
    
    
    
    def addSalesList(self,path="./Sales.csv"):
        '''
        This function adds sales for a given period of time. ( in csv format )
        There is no checking for agreement for dates/times with the current inventory.
        Only items that exist in the Inventory can be sold (and thus passed into this function"
        '''
        #iterate through the sales list csv and populate the sales dict (sales object) with Products
        #for each row in the csv
        #check the ProductId is present in the Inventory
        #check that a key is not currently in the Sales dict.. if not:
        #add the key and the product else add the product to the existing key
        
        

# There must exist error checking as follows

#cannot add a saleslist without an inventory
#cannot add items in the Sales list that do not exist in the inventory
