'''
Created on 24 Jan 2016

@author: Craig
'''
from product import Product
from salesProductList import SalesProductList
from storeInventory import StoreInventory
from ordersList import OrdersList


if __name__ == '__main__':
    inv=StoreInventory()
    inv.addProductsCSV("./csvs/ifix-stock_2016-01-22.csv")
 
 
    sales=SalesProductList()
    sales.addProductsCSV("./csvs/stock-sales_TEST.csv")
    print sales["602"].totalCost
    print sales["602"].retail
    print sales["602"].count
     
    orders=OrdersList()
    orders.addProductsCSV("./csvs/stock-purchases_TESTsmall.csv")
     
 
    inv.addOrders(orders)
    inv.addSales(sales)
#     
    
    #--Stock--
    #total quantity of SKU item in stock
    #total retail value of SKU item in stock
    #total profit for in stock SKU item
    
    #--Orders--
    #total orders for SKU item
    
    #--Sales--
    #total cost of goods sold
    #total cost of sales for SKU
    #total retail for SKU sales

