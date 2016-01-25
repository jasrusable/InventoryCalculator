
from salesProductList import SalesProductList
from product import Product
from salesAddBehaviour import SalesAddBehavior


class TestSales:

    def test_readAndSum(self):

        sold=SalesProductList()
        sold.addProductsCSV("./csvs/stock-sales_TEST.csv")
        
        eA = Product()
        eA.setAddStyle(SalesAddBehavior())
        eA=eA.addStyle.addItem(eA, -4, 5, 10) #calculated manually

        assert sold['602'].totalCost == eA.totalCost
        assert sold['602'].count == eA.count
        assert sold['602'].retail == eA.retail