import plotly_express as px
import dash
from dash import dcc, html
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from Load_data import covid19_sex, covid19_region, covid19_age, vaccin_län, vaccin_ålder, world_data, world_death_country,world_cases_country



stylesheets = [dbc.themes.MATERIA]
app = dash.Dash(__name__)


app.layout = dbc.Container([

        html.Div([
                
                html.H1 (children = 'Covid 19 World Statistics',
                style = {'backgroundColor':'#111111',
                        "textAlign":"center", 
                         "color":"#f5fcff",
                        "height": "50px",
                        "display": "inline-block",
                        "position": "absolute",
                        "top": "50%",
                        "left": "50%",
                        "transform": "translate(-50%, -50%)"}
                )
               ]),
     html.Div([
                html.P("Choose a parameter:"),
                dcc.RadioItems(id='parameter', 
                               className='m-1', value='cases',
                               options=[{'value': x, 'label': x} for x in ['cumulative_count']],
                               labelStyle= {'display': 'inline-block'}
                        ),

                dcc.Graph(id="map-world")], 
                          style= {"width":"100%",
                                   "height": "50px",
                                  "display": "inline-block",
                                  "position": "absolute",
                                  "top": "360%",
                                  "left": "70%",
                                  "transform": "translate(-50%, -50%)"}
                        )
])


world_data= px.data.election()
geojson= px.data.election_geojson()

@app.callback(Output("map-world", "figure"),
              Input("parameter", "value"))


def map_world(indicator):
    fig6= px.choropleth(world_cases_country, geojson = geojson, color='cumulative_count',
          locations="country", featureidkey="properties.district", 
          projection="mercator", range_color=[0, 6500])
    fig6.update_geos(fitbounds="locations", visible=False)
    fig6.update_layout(margin={"r":0, "t":0, "l":0, "b":0})
    
    fig7= px.choropleth(world_death_country, geojson = geojson,color='cumulative_count',
          locations="country", featureidkey="properties.district", 
          projection="mercator", range_color=[0, 6500])
    fig7.update_geos(fitbounds="locations", visible=False)
    fig7.update_layout(margin={"r":0, "t":0, "l":0, "b":0}) 
    
    if indicator=="cases":
            return fig6
    if indicator=="death":
            return fig7