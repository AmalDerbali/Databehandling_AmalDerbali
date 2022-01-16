import pandas as pd
import plotly_express as px
import dash
from dash import dcc, html
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
import plotly.graph_objects as go




covid19_sex = pd.read_excel("C:/Users/Amal Derbali/Documents/GitHub/Databehandling_AmalDerbali/Lab/Data/Folkhalsomyndigheten_Covid19.xlsx", sheet_name ="Totalt antal per kön")
covid19_region = pd.read_excel("C:/Users/Amal Derbali/Documents/GitHub/Databehandling_AmalDerbali/Lab/Data/Folkhalsomyndigheten_Covid19.xlsx", sheet_name="Totalt antal per region")



symbol_dict = dict(Totalt_antal_fall= "Total number of cases",
                   Totalt_antal_avlidna = "Total number of death",
                   Totalt_antal_intensivvårdade ="Total number with intesive care")
covid_dropdown_options = [{"label": name, "value": symbol} 
                     for name, symbol in symbol_dict.items()]





stylesheets = [dbc.themes.MATERIA]
app = dash.Dash(__name__)


#set a title based on: https://www.topcoder.com/thrive/articles/creating-interactive-dashboards-using-plotly-dash
app.layout = dbc.Container([

html.Div(
        style = {'backgroundColor':'#111111'}, children =[
        html.H1 (children = 'Covid 19 Statistics in Sweden',
        style = {'textAlign':'center', 'color':'#f5fcff'}
                )
            ]),

html.Div(
        style = {'backgroundColor':'#111111'}, children =[
        html.H1 (children = 'Number of cases distribution and vaccination progress', 
        style= {'textAlign':'center', 'color':'#f5fcff'})
        ]),

html.Div([
        
                 
        html.P("Choose a statistic:"),
        dcc.Dropdown(id='values', value='Totalt_antal_fall',
                              options=[{'value': x, 'label': x} for x in ['Totalt_antal_fall','Totalt_antal_avlidna', 'Totalt_antal_intensivvårdade']],
                 clearable=False),
        
        
html.Div([
                 
        html.P("Number of cases based on gender", style={'font-size': '25px'}),
       
        dcc.Graph(id="graph-pie"),
             ], style= {'width':'40%', 'display':'inline-block'}),



html.Div([

         html.P("Number of cases based on region", style={'font-size': '25px'}),
        
        dcc.Graph(id="graph-bar"),
             ], style= {'width':'60%', 'display':'inline-block'})    
        ])

])


   

#bar charts based on: https://plotly.com/python/bar-charts/
@app.callback(Output("graph-pie", "figure"),
              Input("values", "value"))

def pie_chart(values):
    fig1 = px.pie(covid19_sex, values=values, color_discrete_sequence=px.colors.sequential.Plasma)
    return fig1


@app.callback(Output("graph-bar", "figure"),
              Input("values", "value"))

def bar_chart(values):
    fig2 = px.bar(covid19_region, x=values, y="Region", color=values)
    return fig2






if __name__ == '__main__':
  app.run_server(debug = True)