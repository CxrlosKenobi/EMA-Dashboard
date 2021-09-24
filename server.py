import dash
import dash_html_components
import dash_bootstrap_components as dbc
import os

FA = "https://use.fontawesome.com/releases/v5.15.1/css/all.css"
LOGO = "./assets/CC_ICON.png"

app = dash.Dash(
	__name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP, FA],
	meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)
app.title = "EMA CC"

server = app.server
app.config.suppress_callback_exceptions = True
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True