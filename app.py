from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import plotly
import dash

from server import app, server
from views import home
import sys

content = html.Div(id="page-content", className="content")

app.layout = html.Div(
    [dcc.Location(id="url"), home.layout, content]
)

if __name__ == '__main__':
    app.run_server(
        host='127.0.0.1', 
        port='2021', 
        debug=True
    )

