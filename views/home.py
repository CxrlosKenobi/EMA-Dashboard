from dash import html, dcc
from dash.dependencies import Input, Output, State
import plotly
import dash

from server import app, server
from views import home
from API.api import *
import os

app_color = {"graph_bg": "#082255", "graph_line": "#007ACE"}
GRAPH_INTERVAL = os.environ.get("GRAPH_INTERVAL", 1000)


layout = html.Div([ # Main div
    html.Div([ # Main Section div
        html.Div([ # Header div 1
            html.H4 (
                'EMA - Estación de Monitoreo Ambiental',
                className='appHeaderTitle'
            ),
            html.P(
                'Comunidad Nacional de Ciencia e Innovación (CON-CIENCIA)',
                className='appHeaderTitle gray',
            ),
        ], className='app__header__desc'),
        html.Div([
            html.A(href='https://con-ciencia.cl/'),
            html.Img(
                src=app.get_asset_url('https://con-ciencia.cl/web/image/website/4/logo/Comunidad%20CON-CIENCIA?unique=c91f8b4'),
                className='app__menu__img',
            )
        ], className='app__header__logo'),
    ], className='AppHeader'),

    html.Div([ # Main Section div 2
        html.Div([ # Graph container
            html.Div([
                html.Div([ # Header div
                    html.H6(
                        'Material Particulado en el Aire [ppm]',
                        className='graph__title'
                    )
                ]),
                dcc.Graph(
                    id='graph-live',
                    figure=dict(
                        layout=dict(
                            plot_bgcolor=app_color['graph_bg'],
                            paper_bgcolor=app_color['graph_bg'],
                        ),
                    ),
                ),
                dcc.Interval(
                    id='graph-update',
                    interval=int(GRAPH_INTERVAL),
                    n_intervals=0
                ),
            ], className='two-thirds column wind__speed__container'),
        ])
    ]),
], className='MainContainer')

@app.callback(
    Output('graph-live', 'figure'), [Input('graph-update', 'n_intervals')]
)
def updateFigure(n):
    # total_time = get_current_time()
    # df0 = get_hdc_te_data(total_time - 200, total_time)
    # df1 = get_hdc_hu_data(total_time - 200, total_time)

    PM25 = dict(
        name='Temperatura (C°)',
        type="scatter",
        y=df0["hdc1080_te"],
        line={"color": "#00BB2D"},
        mode="lines",
    )
    PM10 = dict(
        name='Humedad (%)',
        type="scatter",
        y=df1["hdc1080_hu"],
        line={"color": "#42C4F7"},
        mode="lines",
    )

    layout = dict(
        plot_bgcolor=app_color["graph_bg"],
        paper_bgcolor=app_color["graph_bg"],
        font={"color": "#fff"},
        height=250,
        autosize=True,
        showlegend=False,
        xaxis={
            "range": [0, 200],
            "showline": True,
            "zeroline": False,
            "fixedrange": True,
            "tickvals": [0, 50, 100, 150, 200],
            "ticktext": ["200", "150", "100", "50", "0"],
            "title": "Tiempo transcurrido (seg)",
        },
        yaxis={
            "range": [
                min(min(df0["hdc1080_te"]), min(df1['hdc1080_hu'])),
                max(max(df0["hdc1080_te"]), max(df1['hdc1080_hu'])),
            ],
            "showgrid": True,
            "showline": True,
            "fixedrange": True,
            "zeroline": False,
            "gridcolor": app_color["graph_line"],
        },
    )

    return {'data': [PM25, PM10], 'layout': layout}