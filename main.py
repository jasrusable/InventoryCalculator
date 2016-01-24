'''
Created on 24 Jan 2016

@author: Craig
'''
from product import Product
from salesProductList import SalesProduct
from storeInventory import StoreInventory
from ordersList import OrdersList


if __name__ == '__main__':
    inv=StoreInventory()
    inv.addProducts("./csvs/ifix-stock_2016-01-22.csv")
    print inv['3346'].cost
    
    sales=SalesProduct()
    sales.addProducts("./csvs/stock-sales_2016-01-16_to_2016-01-22.csv")
    print inv['3346'].cost
    
    orders=OrdersList()
    orders.addProducts("./csvs/stock-purchases_2016-01-16_to_2016-01-22.csv")
    print orders['3346'].count