import pandas as pd

import dash
from dash import dash_table
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

from energy_consumption import data

app = dash.Dash(__name__,
                meta_tags=[{
                    "name": "viewport",
                    "content": "width=device-width, initial-scale=1",
                    'charSet': '“UTF-8”'
                }])

app.title = "Energy Consumption"

app.layout = html.Div(

    [
        # Banner ------------------------------------------------------------
        html.Div(
            [
                html.A(
                    [
                        html.Img(
                            src="/assets/images/energy_icon.png",
                            alt="World Energy"
                        ),
                        html.H3("World Energy")
                    ],
                    href="#",
                    target='_blank',
                    className="logo-banner",
                ),
                html.Div(
                    [
                        html.A(
                            "Documentation",
                            href="#",
                            target='_blank',
                            className="doc-link"
                        ),
                        html.A(
                            "Contribute",
                            href="https://github.com/Joannaakl27/",
                            target='_blank',
                            className="doc-link"
                        ),
                        html.Button(
                            "Download data",
                            className="doc-link-download",
                            id = "btn-download-data",
                            n_clicks= 0
                        ),
                        dcc.Download(id="download-csv")

                    ],
                    className="navbar"
                ),
            ],
            className="banner",
        ),

    dcc.Store(id='store-energydata', data = data.read_json_data('../raw_data/world_energy_consumption_json.json'), storage_type = 'memory')
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=True)
