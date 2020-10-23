import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_table

import pandas as pd
import numpy as np
import json

SUPP_LOGO = "/assets/logos/Logo_supplier_v2.gif"
# Section layout --------------------

layout = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            'BIENVENIDOS A SUPPLIER',
                            className='mb-5 display-4 font-weight-bold text-home-title text-light font-medium title-visor',
                        ),
                        html.Div(
                            [
                                html.P(
                                    """
                                    ¡SOMOS UN GRUPO EFECTIVO PARA LA PREDICCIÓN DE DEMANDA DE SUS ARTÍCULOS DE VENTA POR CATÁLOGO EN SU EMPRESA!
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
        html.A(
            html.Div(
                [
                    html.Img(src=SUPP_LOGO, height="200px"),
                ],
                className='mr-5',
            ),
            href="/prediccion",
            className = 'position-relative overflow-hidden text-center',
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            'CON EL APOYO DE:',
                            className='row mb-2 display-4 font-weight-bold text-home-title mx-auto justify-content-center font-medium',
                        ),
                        html.Div(
                            [
                            dbc.Row(
                                [
                                dbc.Col(
                                html.A(
                                    [
                                        html.Div(
                                            [
                                                html.Img(src='/../assets/logos/OFFCORSS.gif', className='div-for-image-offcorss')
                                            ],
                                            className='col'
                                        ),
                                    ],
                                    href="https://www.offcorss.com/",
                                ),xs=10, sm=5, md=5, lg=6, xl=4
                                ),
                                dbc.Col(
                                html.A(
                                    [
                                        html.Div(
                                            [
                                                html.Img(src='/../assets/logos/correlation_one.gif', className='div-for-image-correlation')
                                            ],
                                            className='col'
                                        ),
                                    ],
                                    href="https://www.correlation-one.com/",
                                ), xs=10, sm=5, md=5, lg=6, xl=4
                                ),
                                dbc.Col(
                                html.A(
                                    [
                                        html.Div(
                                            [
                                                html.Img(src='/../assets/logos/mintic.png', className='div-for-image-mintic')
                                            ],
                                            className='col'
                                        ),
                                    ],
                                    href="https://www.mintic.gov.co/portal/inicio/",
                                ),xs=10, sm=5, md=5, lg=6, xl=4
                                ),
                                ],
                                ),
                            ],
                            className='row align-items-center justify-content-center'
                        ),
                    ],
                    className = 'container pt-5 mt-2'
                ),
    ],
        ),
    ],
)