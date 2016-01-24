
from salesProductList import SalesProduct
from product import Product


class TestSales:
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_readAndSum(self):

        sold=SalesProduct()
        sold.addProducts("./csvs/stock-sales_TEST.csv")
        expected = Product()
        expected.addItem(-10, (92.0*7-100), 299)
        assert int(sold['3346'].cost) == expected.cost
        assert int(sold['3346'].count) == expected.count
        assert int(sold['3346'].retail) == expected.retail