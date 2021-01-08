# The following code gets the financial data from 
import yfinance as yf

class stock_markets():

    def get_one_stock(self,stock,periodicity="1d"):
        ticker_holder = yf.Ticker(stock)
        print("###-----",stock,"-----###")
        return(ticker_holder.history(period=periodicity))
    
    def get_many_stocks(self,stock,periodicity="1d"):    
        ticker_holder = yf.Tickers(stock)
        print("###-----",stock,"-----###")
        return(ticker_holder.history(period=periodicity))
    
    def get_stock_info(self,stock,periodicity="1d"):
        #---Only one stock at the time
        ticker_holder = yf.Ticker(stock)
        print("###-----Bussines Summary ",stock,"-----###")
        try: 
            hstr = ticker_holder.info
            return hstr["longBusinessSummary"]
        except IndexError:
            return False # This allow us to control unittest wrong_stock_symbol

if __name__ == "__main__":

        
    #Initialization

    stock_init = stock_markets()

    stock = "MSFT"
    stocks = ["TSLA", "MSFT", "AAPL"]
    print(stock_init.get_one_stock(stock))
    print(stock_init.get_one_stock(stock,"2d"))
    print(stock_init.get_many_stocks(stocks))
    

    