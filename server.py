from dash import dash
import dash_bootstrap_components as dbc

FA = "https://use.fontawesome.com/releases/v5.15.1/css/all.css"
LOGO = "https://con-ciencia.cl/web/image/website/4/logo/Comunidad%20CON-CIENCIA?unique=c91f8b4"

app = dash.Dash(
	__name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP, FA],
	update_title="Cargando datos...",
	meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)
app.title = "EMA"

server = app.server
app.config.suppress_callback_exceptions = True
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True
