import pandas as pd
import plotly_express as px
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from dataframe_function import StockData

covid19 = StockData() 
#= pd.read_excel("C:/Users/Amal Derbali/Documents/GitHub/Databehandling_AmalDerbali/Lab/Covid_dashbord/Covid19_vecka.xlsx")

symbol_dict = dict(Antal_fall_vecka ="New cases per week",
                   Antal_avlidna_vecka ="Death per week",
                   Kum_antal_fall ="Cumulative cases per week")

dropdown_options = [{"label": name, "value": symbol} 
                     for name, symbol in symbol_dict.items()]
df_dict ={symbol:covid19.stock_dataframe(symbol) 
          for symbol in symbol_dict}

slider_marks ={t : str(Vecka) for t, Vecka in range (covid19["Vecka"], 5)}

stylesheets = [dbc.themes.MATERIA]
app = dash.Dash(__name__, external_stylesheets = stylesheets, 
                meta_tags=[dict(name ="viewport", content ="width=device-width, initial-scale=1.0")])







# Create figure and change bgc based on : https://plotly.com/python/images/
fig = go.Figure()

# Set templates
fig.update_layout(paper_bgcolor="black")

fig.show()