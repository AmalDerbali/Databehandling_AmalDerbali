import pandas as pd
import plotly_express as px
import dash
from dash import dcc, html
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
import plotly.graph_objects as go




covid19_sex = pd.read_excel("C:/Users/Amal Derbali/Documents/GitHub/Databehandling_AmalDerbali/Lab/Data/Folkhalsomyndigheten_Covid19.xlsx", sheet_name ="Totalt antal per kön")
covid19_region = pd.read_excel("C:/Users/Amal Derbali/Documents/GitHub/Databehandling_AmalDerbali/Lab/Data/Folkhalsomyndigheten_Covid19.xlsx", sheet_name="Totalt antal per region")
covid19_age = pd.read_excel("C:/Users/Amal Derbali/Documents/GitHub/Databehandling_AmalDerbali/Lab/Data/Folkhalsomyndigheten_Covid19.xlsx", sheet_name="Totalt antal per åldersgrupp")

vaccin_df = pd.read_excel("C:/Users/Amal Derbali/Documents/GitHub/Databehandling_AmalDerbali/Lab/Data/Folkhalsomyndigheten_Covid19_Vaccine.xlsx", sheet_name="Vaccinerade kommun och ålder")
vaccin_län = vaccin_df.groupby("Län_namn").mean().reset_index()
vaccin_age = vaccin_df.groupby("Ålder").mean().reset_index()

world_data = pd.read_excel("data/Uppgift_4_world_data.xlsx", sheet_name="Sheet1")
world_cases = world_data[world_data["indicator"] == "cases"].reset_index(drop=True)
world_cases_country = world_cases.groupby("country").mean().reset_index()
world_death = world_data[world_data["indicator"] == "deaths"].reset_index(drop=True)
world_death_country = world_death.groupby("country").mean().reset_index()



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
                 
        html.P("Number of cases based on gender:", style={'font-size': '25px'}),
       
        dcc.Graph(id="graph-pie"),
             ], style= {'width':'40%', 'display':'inline-block'}),


html.Div([

         html.P("Number of cases based on region:", style={'font-size': '25px'}),
        
        dcc.Graph(id="graph-bar"),
             ], style= {'width':'60%', 'display':'inline-block'})    
        ]),

html.Div([
        html.P("Number of cases per age:", style={'font-size': '25px'}),

        html.P("Choose a statistic:"),

        dcc.Dropdown(id='val', value='Totalt_antal_fall',
                     options=[{'value': x, 'label': x} 
                     for x in ['Totalt_antal_fall','Totalt_antal_avlidna', 'Totalt_antal_intensivvårdade']]),

        dcc.Graph(id="graph-histogram")],
                  style= {'width':'70%',
                         "height": "50px",
                         "display": "inline-block",
                         "position": "absolute",
                         "top": "115%",
                         "left": "50%",
                         "transform": "translate(-50%, -50%)"}),
        
dbc.Row([
        html.P("Number of vaccinated people in Sweden:", style={'font-size': '25px'}),       
        
        dbc.Col(
                html.P("Choose:"), className='m-1', xl={"size": 2, "offset": 2}),
        
        dbc.Col(
                dbc.Card(
                        dcc.RadioItems(id= 'vaccin', className='m-1',
                        value='Län_namn',
                        options=[{'value': x, 'label': x} for x in ['Län_namn','Ålder']]
                        )) 
                    
                ),
                dcc.Graph(id="graph-bar-vaccin")], style= {'width':'70%',
                         "height": "50px",
                         "display": "inline-block",
                         "position": "absolute",
                         "top": "200%",
                         "left": "50%",
                         "transform": "translate(-50%, -50%)"}),

html.Div(
        style = {'backgroundColor':'#111111'}, children =[
        html.H1 (children = 'Covid 19 World Statistics',
        style = {'textAlign':'center', 'color':'#f5fcff'}
                )
            ]),


])
       
        



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


@app.callback(Output("graph-histogram", "figure"),
              Input("val", "value"))

def histogram(val):
        fig3= px.histogram(covid19_age, x="Åldersgrupp", y=val,
        color_discrete_sequence=px.colors.sequential.Rainbow)
        return fig3


@app.callback(Output("graph-bar-vaccin", "figure"),
              Input("vaccin", "value"))

def bar_vaccin(vaccin):
    fig4 = px.bar(vaccin_län, x= "Län_namn", y=["Andel minst 1 dos", "Andel färdigvaccinerade"],
                  color_discrete_sequence=px.colors.sequential.Inferno, barmode="group")
    fig5 = px.bar(vaccin_age, x= "Ålder", y=["Andel minst 1 dos", "Andel färdigvaccinerade"],
                  color_discrete_sequence=px.colors.sequential.Inferno, barmode="group")
    if vaccin=="Län_namn":
            return fig4
    if vaccin=="Ålder":
            return fig5



if __name__ == '__main__':
  app.run_server(debug = True)


#modify colors according to :https://www.sharpsightlabs.com/blog/plotly-histogram/
#bar charts modifications based on: https://plotly.com/python/bar-charts/
#change figure position based on :https://stackoverflow.com/questions/65662293/how-to-center-a-dash-graph
