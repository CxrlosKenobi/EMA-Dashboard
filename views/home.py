from dash import html, dcc
from dash.dependencies import Input, Output, State
import plotly
import dash
import numpy as np

from server import app, server
from views import home
from API.api import *
import random
import os

app_color = {"graph_bg": "#082255", "graph_line": "#007ACE"}
GRAPH_INTERVAL = os.environ.get("GRAPH_INTERVAL", 1000)


layout = html.Div([ # Main div
    html.Div([ # Main Section div
        html.Div([ # Header div 1
            html.H4 (
                'EMA - Estación de Monitoreo Ambiental',
                className='AppHeaderTitle'
            ),
            html.P(
                'Comunidad Nacional de Ciencia e Innovación (CON-CIENCIA)',
                className='AppHeaderTitle gray',
            ),
        ], className='AppHeaderDesc'),
        html.Div([
            html.A(href='https://con-ciencia.cl/'),
            html.Img(
                src=app.get_asset_url('https://con-ciencia.cl/web/image/website/4/logo/Comunidad%20CON-CIENCIA?unique=c91f8b4'),
                className='LogoIcon',
            )
        ], className='AppHeaderLogo'),
    ], className='AppHeader'),

    html.Div([ # Main Section div 2
        html.Div([ # Graph container
            html.Div([
                html.Div([ # Header div
                    html.H6(
                        'Material Particulado en el Aire [ppm]',
                        className='graphTitle'
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
            ], className='two-thirds column mainGraphContainer'),
        ])
    ]),
], className='MainContainer')


@app.callback(
    Output('graph-live', 'figure'), [Input('graph-update', 'n_intervals')]
)
def updateFigure(n):
    total_time = get_current_time()
    # df0 = get_hdc_te_data(total_time - 200, total_time)
    # df1 = get_hdc_hu_data(total_time - 200, total_time)

    df = dataReader()

    # Trace 0
    PM25 = dict(
        name='PM 2.5',
        type="data",
        y=df[2],
        line={"color": "#FC0000"},
        mode="lines",
        fillcolor='rgba(69, 214, 255, 0.5)',
    )

    # Trace 1
    PM10 = dict(
        name='PM 10',
        type="data",
        y=df[3],
        line={"color": "#45D6FF"},
        mode="lines",
        fillcolor='rgba(69, 214, 255, 0.5)',
    )

    layout = dict(
        height=500,
        plot_bgcolor=app_color["graph_bg"],
        paper_bgcolor=app_color["graph_bg"],
        font={"color": "#fff"},
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
                0, 100,
                0, 100,
            ],
            "showgrid": True,
            "showline": True,
            "fixedrange": True,
            "zeroline": False,
            "gridcolor": app_color["graph_line"],
        },
    )

    return {'data': [PM25, PM10], 'layout': layout}
