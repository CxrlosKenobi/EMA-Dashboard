from dash import dcc, html
from server import app
from views import home

content = html.Div(id="page-content", className="Content")

app.layout = html.Div(
    [dcc.Location(id="url"), home.layout, content]
)

if __name__ == '__main__':
    app.run_server(
        host='127.0.0.1', 
        port='2021', 
        debug=True
    )
