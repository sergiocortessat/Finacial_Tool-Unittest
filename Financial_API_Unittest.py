import unittest2
from Get_Fiancial_API import *

class financial_test(unittest2.TestCase):

    def setUp(self):
        self.temp_stock_markets = stock_markets()
        self.correct_symbols = ["AAPL","TSLA","MCFT","IBMG"]
        self.incorrect_symbols = ["APPLS","MRTG","IBHG"]
    
    def tearDown(self):
        self.temp_stock_markets
    

    def test_onestock_fetching(self):
        for stock in self.correct_symbols:
            temp_stock = self.temp_stock_markets.get_one_stock(stock)
            self.assertFalse(temp_stock.empty,"The data is not fetched properly using correct Symbols")

    def test_wrong_onestock_fetching(self):
        for stock in self.incorrect_symbols:
            temp_stock = self.temp_stock_markets.get_one_stock(stock)
            self.assertTrue(temp_stock.empty)
        
    def test_multistock_fetching(self):
        self.assertFalse(self.temp_stock_markets.get_many_stocks(self.correct_symbols).empty)
    
    def test_wrong_multistock_fetching(self):
        self.assertTrue(self.temp_stock_markets.get_many_stocks(self.incorrect_symbols).empty)
    
    def test_company_info(self):
        temp_stock = "TSLA"
        self.assertIsInstance(self.temp_stock_markets.get_company_info(temp_stock),str)

    def test_failedcompany_info(self):
        temp_stock = "TSLAA"
        try: #I must perfrom a Try, Except. An incorrect stock name will thro an IndentError due to method get_company_info due to method .info of yfiance.
            self.temp_stock_markets.get_company_info(temp_stock)
        except IndexError:
            self.assertRaises(IndexError)


if __name__ == "__main__":
    unittest2.main()  