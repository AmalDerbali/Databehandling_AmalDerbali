import plotly_express as px
import dash
from dash import dcc, html
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
from Load_data import world_cases_continent, world_death_continent




stylesheets = [dbc.themes.MATERIA]
app = dash.Dash(__name__)

#chart based on : https://plotly.com/python/line-and-scatter/


app.layout = dbc.Container([
    html.Div([
                
                html.H1 (children = 'Covid 19 World Statistics',
                style = {'backgroundColor':'#111111',
                        "textAlign":"center", 
                         "color":"#f5fcff",
                        "height": "50px",
                        "display": "inline-block",
                        "position": "absolute",
                        "top": "0%",
                        "left": "50%",
                        "transform": "translate(-50%, -50%)"}
                )
               ]),



    html.Div([
    dcc.Graph(id="scatter-world"),
    dcc.RangeSlider(id='slider', min=0, max= 51000, 
                    step=100, marks={0:'0', 51000: '51000'},
                    value= [100, 1000])
    ])
])

@app.callback(
    Output("scatter-world", "figure"),
    Input("slider", "value"))

def uptade_chart(slider):
    low, high = slider
    mask= (world_cases_continent['cumulative_count'] > low) & (world_cases_continent['cumulative_count'] > high)
    fig= px.scatter(
        world_cases_continent[mask], x="cumulative_count", y="continent",
        color="continent", size='cumulative_count', hover_data=['cumulative_count'])
    return fig

if __name__ == '__main__':
  app.run_server(debug = True)
    
