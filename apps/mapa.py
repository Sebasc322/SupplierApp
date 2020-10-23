
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_table

import plotly.express as px
from plotly import graph_objs as go
from urllib.request import urlopen
import json

# Loading dataframes
# from data import df_national_covid, df_summary


# GRAPHS ----------------------

# 1. Colombia cloropleth map: Number of contracts per department

with urlopen('https://gist.githubusercontent.com/john-guerra/43c7656821069d00dcbc/raw/3aadedf47badbdac823b00dbe259f6bc6d9e1899/colombia.geo.json') as response:
    departments = json.load(response)

#fig_map_2 = px.choropleth_mapbox(df_national_covid,
            #               geojson=departments,
           #                locations='Code',
          #                 color='Num. contratos',
         #                  featureidkey='properties.DPTO',
        #                   hover_name='Departamento',
       #                    color_continuous_scale="Mint",
      #                     range_color=(0, max(df_national_covid['Num. contratos'])),
     #                      mapbox_style="carto-positron",
    #                       zoom=4,
   #                        center = {"lat": 4.570868, "lon": -74.2973328},
  #                         opacity=0.5
 #                         )
#fig_map_2.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# 1. Colombia cloropleth map: value of contracts per department
#fig_map_cuantia = px.choropleth_mapbox(df_national_covid,
        #                   geojson=departments,
       #                    locations='Code',
      #                     color='Total cuantía contratos',
     #                      featureidkey='properties.DPTO',
    #                       hover_name='Departamento',
   #                        color_continuous_scale="Peach",
  #                         range_color=(min(df_national_covid['Total cuantía contratos'])-10000000, max(df_national_covid['Total cuantía contratos'])),
 #                          mapbox_style="carto-positron",
#                           zoom=4,
#                           center = {"lat": 4.570868, "lon": -74.2973328},
#                           opacity=0.5
#                          )
#fig_map_cuantia.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# 1. Colombia cloropleth map: Number of contracts per department
#fig_summary = px.bar(df_summary, x="Número de alertas", y="Alerta", orientation='h',
#             height=500)
#fig_summary.update_layout(
#    font=dict(
#        color="#252525",
#        family="Roboto"
#    ),
#    paper_bgcolor='rgba(0,0,0,0)',
#    plot_bgcolor='rgba(0,0,0,0)',
#    xaxis_title="Numero de contratos con alertas",
#    yaxis_title='',
#    margin={"r":0,"t":0,"l":0,"b":0}
#)


layout = html.Div(
    [
        html.Div(
            [
                        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            'MAPA DE COLOMBIA',
                            className='mb-5 display-4 font-weight-bold text-home-title text-light font-medium title-visor',
                        ),
                        html.Div(
                            [
                                html.P(
                                    """
                                    En esta sección pueden encontrar la distribución de vendedoras y top artículos demandados por departamento en Colombia.
                                    """,
                                    className='lead font-weight-normal text-light font-home-m'
                                ),
                            ],
                            className='mb-5',
                        ),
                    ],
                    className='col-md-5 p-lg-5 mx-auto my-5',
                ),
            ],
            className = 'position-relative overflow-hidden text-center back-home',
        ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    'Catálogo Moda en Colombia para la venta directa',
                                    className='row mb-2 display-4 font-weight-bold text-home-title mx-auto justify-content-center font-medium',
                                ),
                                html.Div(
                                    [
                                        html.P(
                                            """
                                            Vendedoras por departamento y top items vendidos.
                                            """
                                        ),
                                    ],
                                    className='text-left pl-5 pr-5 text-center'
                                ),
                                dcc.Tabs(
                                    value = 'num_vendedoras',
                                    colors={
                                        "border": "white",
                                        "primary": "#59a0f1 ",
                                        "background": "#daecf5"
                                    },
                                    parent_className='div-for-tab',
                                    children=[
                                        dcc.Tab(
                                            label = 'Por número de vendedoras',
                                            value = 'num_vendedoras',
                                            children=[
#                                                dcc.Graph(figure=fig_map_2, className='div-for-graph-border')
                                            ],
                                            className='div-for-tab',
                                            selected_className='font-weight-bold',
                                        ),
                                        dcc.Tab(
                                            label = 'Por top artículos',
                                            value = 'top_articulos',
                                            children=[
#                                                dcc.Graph(figure=fig_map_cuantia, className='div-for-graph-border')
                                            ],
                                            className='div-for-tab',
                                            selected_className='font-weight-bold',
                                        )
                                    ]
                                )
                            ],
                            className='col div-for-graph-card'
                        ),
                    ],
                    className='row',
                ),
            ],
            className='mb-5',
        ),
    ],
)