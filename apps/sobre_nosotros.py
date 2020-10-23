import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_table

from app import app

TEAM_LOGO = "/assets/logos/TEAM_100.gif"

layout = html.Div(
            [
            html.A(
                html.Div(
                [
                    html.Img(src=TEAM_LOGO, height="130px"),
                ],
                className='position-relative overflow-hidden text-center back-home',
            ),
            href="/sobre_nosotros",
            className = 'position-relative overflow-hidden text-center back-home',
        ),
                html.Div(
                    [
                        html.Div(
                            'GRUPO SUPPLIER',
                            className='row mb-2 display-4 font-weight-bold text-home-title mx-auto justify-content-center font-medium',
                        ),
                        html.Div(
                            'Somos un grupo de estudiantes del curso Data Science 4 All / Colombia 2020 patrocinado por el Ministerio de las TIC con la colaboración de Correlation One,'
                            ' para preparar colombianos para el futuro digital y la ciencia de datos. Que junto a Offcorss hicimos y entrenamos un modelo de Machine Learning para el pronóstico' 
                            ' de demanda por tipo de prenda y finalmente pronosticar el UPE por tipo de prenda para así poder hacer el pedido a producción',
                            className='row mx-auto justify-content-center text-home-paragraph',
                        ),
                    ],
                    className = 'container pt-5 mt-2'
                ),
            html.Div(
                [
                    dbc.Row(
                        [
                        dbc.Col(
                            html.Div(
                                [
                                    html.Img(src='/../assets/team_100/sebastian.jpg', className='div-for-image-team'),
                                    html.Div('Sebastián Carmona Ángel',className='font-weight-bold text-names-team font-medium'),
                                    html.Div(
                                        'Ingeniero de Petróleos, Especialista en Negocios Internacionales y Data Scientist',
                                        className='text-subtitle-team'),
                                    html.Div(
                                        html.A(
                                            html.I(className="fab fa-linkedin", style={'color': 'grey'}),
                                            href='https://www.linkedin.com/in/sebascarmona/', role="button",
                                        ),
                                        className='social',
                                    ),
                                ],
                                className='div-for-member mx-4'
                            ), xs=10, sm=8, md=5, lg=6, xl=4
                        ),
                        dbc.Col(
                            html.Div(
                                [
                                    #html.Img(src='/../assets/fotos_team/melissa.jpeg', className='div-for-image-team'),
                                    html.Div('Carlos Andres Diaz Cardozo', className='font-weight-bold text-names-team font-medium'),
                                    html.Div(
                                        'Profesional de Gestión de Información',
                                        className='text-subtitle-team'),
                                    html.Div(
                                        html.A(
                                            html.I(
                                                className="fab fa-linkedin", style={'color': 'grey'}),
                                                href='https://www.linkedin.com/in/carlos-andr%C3%A9s-d%C3%ADaz-cardozo-a9312446/', role="button",
                                            ),
                                        className='social',
                                    ),
                                ],
                            className='div-for-member mx-4'
                            ), xs=10, sm=8, md=5, lg=6, xl=4
                        ),
                        dbc.Col(
                            html.Div(
                                [
                                    html.Img(src='/../assets/team_100/juansebastian.jpg', className='div-for-image-team'),
                                    html.Div('Juan Sebastián Rojas Melendez', className='font-weight-bold text-names-team font-medium'),
                                    html.Div('Ingeniero en Electrónica y Telecomunicaciones, Magister y PhD en Ingeniería Telemática y Data Scientist', className='text-subtitle-team'),
                                    html.Div(
                                        html.A(
                                            html.I(
                                                className="fab fa-linkedin", style={'color': 'grey'}),
                                                href='https://www.linkedin.com/in/juan-sebasti%C3%A1n-rojas-mel%C3%A9ndez-502684108/', role="button",
                                            ),
                                        className='social',
                                    ),
                                ],
                            className='div-for-member mx-4'
                            ), xs=10, sm=8, md=5, lg=6, xl=4
                        ),
                    ]
                ),
            ],
        className = 'container pt-5 mt-2 mb-5 d-flex justify-content-center'
        ),
                html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            html.Div(
                                [
                                    html.Img(src='/../assets/team_100/ivan.jpg', className='div-for-image-team'),
                                        html.Div('Ivan Darío Peñaranda Arenas', className='font-weight-bold text-names-team font-medium'),
                                        html.Div('Ingeniero Químico y Data Scientist con experiencia en Big Data y Machine Learning', className='text-subtitle-team'),
                                        html.Div(
                                            html.A(
                                                html.I(
                                                    className="fab fa-linkedin", style={'color': 'grey'}),
                                                    href='https://www.linkedin.com/in/ivan-dario-penaranda-arenas-0426b145/', role="button",
                                            ),
                                            className='social',
                                    ),
                                ],
                                className='div-for-member mx-4'
                            ), xs=10, sm=8, md=5, lg=6, xl=4
                        ),
                        dbc.Col(
                            html.Div(
                                [
                                    #html.Img(src='/../assets/fotos_team/carlos.jpeg', className='div-for-image-team'),
                                    html.Div('Rafael Eduardo Campo Hernandez', className='font-weight-bold text-names-team font-medium'),
                                    html.Div('Gerente de Proyectos en Advisers & Consultants SAS', className='text-subtitle-team'),
                                    html.Div(
                                        html.A(
                                            html.I(
                                                className="fab fa-linkedin", style={'color': 'grey'}),
                                                href='https://www.linkedin.com/in/rafael-eduardo-campo-hernandez-a0984651/', role="button",
                                            ),
                                        className='social',
                                    ),
                                ],
                            className='div-for-member mx-4'
                            ), xs=10, sm=8, md=5, lg=6, xl=4
                        ),
                        dbc.Col(
                            html.Div(
                                [
                                    #html.Img(src='/../assets/fotos_team/carlos.jpeg', className='div-for-image-team'),
                                    html.Div('Juan Carlos Lozano Sierra', className='font-weight-bold text-names-team font-medium'),
                                    html.Div('Director de operaciones en Autónomo', className='text-subtitle-team'),
                                    html.Div(
                                        html.A(
                                            html.I(
                                                className="fab fa-linkedin", style={'color': 'grey'}),
                                                href='https://www.linkedin.com/in/juankloz/', role="button",
                                            ),
                                        className='social',
                                    ),
                                ],
                            className='div-for-member mx-4'
                            ), xs=10, sm=8, md=5, lg=6, xl=4
                        ),
                    ]
                ),
            ],
            className = 'container pt-5 mt-2 mb-5 d-flex justify-content-center'
        ),
                html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            html.Div(
                                [
                                    #html.Img(src='/../assets/fotos_team/carlos.jpeg', className='div-for-image-team'),
                                    html.Div('Daniel Alejandro Cano Saenz', className='font-weight-bold text-names-team font-medium'),
                                    html.Div('Estudiante', className='text-subtitle-team'),
                                    html.Div(
                                        html.A(
                                            html.I(
                                                className="fab fa-linkedin", style={'color': 'grey'}),
                                                href='https://www.linkedin.com/in/daniel-cano-5845041b2/', role="button",
                                            ),
                                        className='social',
                                    ),
                                ],
                            className='div-for-member mx-4'
                            ), xs=10, sm=8, md=5, lg=6, xl=12
                        ),
                    ]
                ),
            ],
        className = 'container pt-5 mt-2 mb-5 d-flex justify-content-center'
        ),
    ],
            className = 'position-relative overflow-hidden text-center div-for-quienes-somos',
)