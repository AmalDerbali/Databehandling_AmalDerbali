
#function based on lektion

import pandas as pd
df= pd.read_excel("C:/Users/Amal Derbali/Documents/GitHub/Databehandling_AmalDerbali/Lab/Covid_dashbord/Covid19_vecka.xlsx")
class StockData:
    """Class method to get and process local stock data"""
    def __init__(self, data_path: str = "C:/Users/Amal Derbali/Documents/GitHub/Databehandling_AmalDerbali/Lab/Covid_dashbord/") -> None:
        self._data_path = data_path

def stock_dataframe(self, stockname: str) ->list:
    stock_df = []
    for path_ending in ["Covid19_vecka.xlsx"]:
        path = self._data_path+stockname+path_ending
        stock = pd.read_excel(path, index_col = 0, parse_date = True)
        stock.index.rename("Vecka", inplace=True)
        stock_df.append(stock)
    
    return stock_df
        