import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_table

import pandas as pd
import numpy as np
import json



layout = html.Div(
    [
        html.Div(
            [
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            'PANORAMA ESTADÍSTICO',
                            className='mb-5 display-4 font-weight-bold text-home-title text-light font-medium title-visor',
                        ),
                        html.Div(
                            [
                                html.P(
                                    """
                                    En esta sección podrán ver un análisis estadístico de lo que fueron las campañas 2019-2020 para la venta por catálogo a nivel nacional para Offcorss.
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
            ],
        ),
    ],
)