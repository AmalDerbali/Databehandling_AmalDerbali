import pandas as pd
from dateutil.relativedelta import relativedelta


cov = pd.read_excel("C:/Users/Amal Derbali/Documents/GitHub/Databehandling_AmalDerbali/Lab/Covid_dashbord/Folkhalsomyndigheten_Covid19_veckodata_riket.xlsx")
print(cov.head())

class CovidData:
    def __init__(self, data_folder : str = "C:/Users/Amal Derbali/Documents/GitHub/Databehandling_AmalDerbali/Lab/Covid_dashbord/"):
        self._data_folder = data_folder

    def covid_df (self, value):
        covid_df_list = []
        for path_end in ["Folkhalsomyndigheten_Covid19_veckodata_riket.xlsx"]:
            path = self._data_folder+value+path_end
            covid = pd.read_excel(path, index_col = 0, parse_dates =True)
            covid.index.rename("Time", inplace=True)
            covid_df_list.append(covid)
        return covid_df_list
    
    
    
    
    
    
    
    
def filter_time (df, weeks=0):
    last_week = df.index[0].date()
    start_week = last_week - relativedelta(weeks=weeks)
    df = df.sort_index().loc[start_week:last_week]
    return df
    