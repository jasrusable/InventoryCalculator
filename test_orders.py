
import pytest

from ordersList import OrdersList
from product import Product
from salesProductList import SalesProductList
from storeInventory import StoreInventory


class TestSales:
    def test_assertions(self):
        inv=StoreInventory()
        sales=SalesProductList()
        orders=OrdersList()
        with pytest.raises(AssertionError):
            assert inv.addOrders(sales) 
        with pytest.raises(AssertionError):
            assert inv.addSales(orders) 

        
class TestOrders:
    def test_assertions(self):
        inv=StoreInventory()
        sales=SalesProductList()
        orders=OrdersList()
        with pytest.raises(AssertionError):
            assert inv.addOrders(sales) 
        with pytest.raises(AssertionError):
            assert inv.addSales(orders) 

