import pandas as pd
import plotly_express as px
import dash
from dash import dcc, html


covid19 = pd.read_excel("C:/Users/Amal Derbali/Documents/GitHub/Databehandling_AmalDerbali/Lab/Covid_dashbord/Covid19_vecka.xlsx")

symbol_dict = dict( )