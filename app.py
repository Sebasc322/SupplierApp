import dash

metas = [
    {"name": "viewport", "content": "width=device-width, initial-scale=1.0"},
    {"property": "og:title", "content": "Supplier"},
    {"property": "og:description", "content": "."},
    #{"property": "og:image", "content": "https://raw.githubusercontent.com/grupocanario/canopy-demo/master/canopy_thumbnail.png"},
    #{"property": "og:url", "content": "https://www.proyectocanopy.co/"}
]

app = dash.Dash(
    __name__,
    meta_tags=metas,
    title='Supplier',
    update_title='Cargando...',
    suppress_callback_exceptions=True
)