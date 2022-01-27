
import plotly_express as px
import dash
from dash import dcc, html
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from Load_data import covid19_sex, covid19_region, covid19_age, vaccin_län, vaccin_ålder, world_cases_country, world_death_country
# import data


# set theme and initiate dashboard
stylesheets = [dbc.themes.MATERIA]
app = dash.Dash(__name__)


#set a title based on: https://www.topcoder.com/thrive/articles/creating-interactive-dashboards-using-plotly-dash
app.layout = dbc.Container([
        #set title for the first part of Sweden statistics
        html.Div(
                style = {'backgroundColor':'#111111'}, children =[
                html.H1 (children = 'Covid 19 Statistics in Sweden',
                        style = {'textAlign':'center', 'color':'#f5fcff'}
                )
            ]),
        #set subtitle: discription
        html.Div(
                style = {'backgroundColor':'#111111'}, children =[
                html.H1 (children = 'Number of cases distribution and vaccination progress', 
                         style= {'textAlign':'center', 'color':'#f5fcff'})
        ]),
        #start fig1
        html.Div([
                html.P("Choose a statistic:"),
                dcc.Dropdown(id='values', value='Totalt_antal_fall',
                              options=[{'value': x, 'label': x} 
                              for x in ['Totalt_antal_fall','Totalt_antal_avlidna', 'Totalt_antal_intensivvårdade']]),
        html.Div([
                #set first part of the fig1
                html.P("Number of cases based on gender:", 
                       style={'font-size': '25px'}),
                dcc.Graph(id="graph-pie")], 
                          style= {'width':'40%', 'display':'inline-block'}),
        html.Div([
                #set 2d part of fig1
                html.P("Number of cases based on region:", 
                       style={'font-size': '25px'}),
                dcc.Graph(id="graph-bar")], 
                          style= {'width':'60%', 'display':'inline-block'})    
        ]),
        #start fig3 
        #change figure position based on :https://stackoverflow.com/questions/65662293/how-to-center-a-dash-graph
        html.Div([
                html.P("Number of cases per age:", 
                       style={'font-size': '25px'}),
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
        #start fig4
        dbc.Row([
                html.P("Number of vaccinated people in Sweden:", style={'font-size': '25px'}),       
                dbc.Col(
                        html.P("Choose a parameter:"), className='m-1', xl={"size": 2, "offset": 2}),
                dbc.Col(
                        dbc.Card(
                        dcc.RadioItems(id= 'vaccin', className='m-1', value='Län_namn',
                        options=[{'value': x, 'label': x} for x in ['Län_namn','Ålder']]
                        )) 
                    
                ),
                        dcc.Graph(id="graph-bar-vaccin")], 
                                  style= {'width':'70%',
                                  "height": "50px",
                                  "display": "inline-block",
                                  "position": "absolute",
                                  "top": "210%",
                                  "left": "50%",
                                  "transform": "translate(-50%, -50%)"}
                                ),
        # set the 2d part of the dashboard of world statistics
        html.Div([
                #set the main title
                        html.H1 (children = 'Covid 19 World Statistics',
                        style = {'backgroundColor':'#111111',
                        "textAlign":"center", 
                         "color":"#f5fcff",
                        "height": "50px",
                        "display": "inline-block",
                        "position": "absolute",
                        "top": "300%",
                        "left": "50%",
                        "transform": "translate(-50%, -50%)"}
                ),
        html.Div([
                #set subtitle1 and fig5
                       html.P("  Number of cases per country:", 
                       style={'font-size': '25px'}),
                       dcc.Graph(id="cases-world"),
                       dcc.RangeSlider(id='slider1', min=0, max= 1.698e+6, 
                                        step=1, marks={0:'0', 1.698e+6: '1.698e+6'},
                                        value= [1, 1.698e+6])
                                        ], style= {"width":"50%",
                                   "height": "50px",
                                  "display": "inline-block",
                                  "position": "absolute",
                                  "top": "310%",
                                  "left": "1.5%"
                                  })
       
        ]),
        html.Div([
                #set subtitle2 and fig6
                        html.P("  Number of death per country:", 
                        style={'font-size': '25px'}),
                        dcc.Graph(id="death-world"),
                        dcc.RangeSlider(id='slider2', min=0, max= 1.698e+5, 
                                        step=1, marks={0:'0', 1.698e+5: '1.698e+5'},
                                        value= [0, 1.698e+5])
                                        ], style= {"width":"50%",
                                   "height": "50px",
                                  "display": "inline-block",
                                  "position": "absolute",
                                  "top": "310%",
                                  "left": "50%"
                                  
                                        })
])



@app.callback(Output("graph-pie", "figure"),
              Input("values", "value"))

# set pie in the 1st part of the fig1
def pie_chart(values):
    fig1 = px.pie(covid19_sex, values=values, color_discrete_sequence=px.colors.sequential.Plasma)
    return fig1


@app.callback(Output("graph-bar", "figure"),
              Input("values", "value"))

#set bars of the 2d part in fig1
#horizental bar charts and modifications based on: https://plotly.com/python/bar-charts/
def bar_chart(values):
    fig2 = px.bar(covid19_region, x=values, y="Region", color=values)
    return fig2


@app.callback(Output("graph-histogram", "figure"),
              Input("val", "value"))

def line(val):
        fig3= px.line(covid19_age, x="Åldersgrupp", y=val,
        color_discrete_sequence=px.colors.sequential.Rainbow)
        return fig3


@app.callback(Output("graph-bar-vaccin", "figure"),
              Input("vaccin", "value"))

def bar_vaccin(vaccin):
    fig4 = px.bar(vaccin_län, x= "Län_namn", y=["Andel minst 1 dos", "Andel färdigvaccinerade"],
                  color_discrete_sequence=px.colors.sequential.Inferno, barmode="group")
    fig5 = px.bar(vaccin_ålder, x= "Ålder", y=["Andel minst 1 dos", "Andel färdigvaccinerade"],
                  color_discrete_sequence=px.colors.sequential.Inferno, barmode="group")
    if vaccin=="Län_namn":
            return fig4
    if vaccin=="Ålder":
            return fig5



@app.callback(Output("cases-world", "figure"),
              Input("slider1", "value"))

#scatter figs is based on: https://plotly.com/python/line-and-scatter/
def world_cases(slider1):
        low, high = slider1
        stat= (world_cases_country['cumulative_count'] > low) & (world_cases_country['cumulative_count'] < high)
        fig6= px.scatter(world_cases_country[stat], x="cumulative_count", y="country",
        color="country", size='cumulative_count', hover_data=['cumulative_count'])
        return fig6


@app.callback(Output("death-world", "figure"),
              Input("slider2", "value"))

def world_death(slider2):
        low, high = slider2
        stat= (world_death_country['cumulative_count'] > low) & (world_death_country['cumulative_count'] < high)
        fig7= px.scatter(world_death_country[stat], x="cumulative_count", y="country",
        color="country", size='cumulative_count', hover_data=['cumulative_count'])
        return fig7
#modify colors according to :https://www.sharpsightlabs.com/blog/plotly-histogram/


if __name__ == '__main__':
  app.run_server(debug = True)





