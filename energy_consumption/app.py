import pandas as pd
import numpy as np

import dash
from dash import dcc, html, Input, Output, callback, State

from energy_consumption import data
import plot

#data_json = data.read_json_data(
#                  '../raw_data/world_energy_consumption_json.json')
df = pd.read_json('../raw_data/world_energy_consumption_json.json')

app = dash.Dash(__name__,
                meta_tags=[{
                    "name": "viewport",
                    "content": "width=device-width, initial-scale=1",
                    'charSet': '“UTF-8”'
                }])

app.title = "Energy Consumption"

app.layout = html.Div([
    # Banner ------------------------------------------------------------
    html.Div(
        [
            html.A(
                [
                    html.Img(src="/assets/images/energy_icon.png",
                             alt="World Energy"),
                    html.H3("World Energy")
                ],
                href="#",
                target='_blank',
                className="logo-banner",
            ),
            html.Div([
                html.A("Documentation",
                       href="#",
                       target='_blank',
                       className="doc-link"),
                html.A(
                    "Contribute",
                    href="https://github.com/Joannaakl27/energy_consumption",
                    target='_blank',
                    className="doc-link"),
                html.Button("Download data",
                            className="doc-link-download",
                            id="btn-download-data",
                            n_clicks=0),
                dcc.Download(id="download-csv")
            ],
                     className="navbar"),
        ],
        className="banner",
    ),

    # Content ------------------------------------------------------------

    #    dcc.Store(id='store-energydata',
    #              data=data.read_json_data(
    #                 '../raw_data/world_energy_consumption_json.json'),
    #              storage_type='memory'),
    html.Div([
        dcc.Dropdown(id='country-dropdown',
                     options= np.append(["All"],
                                       df["country"].unique()).tolist(),
                     value="All"),
        html.Div(id='plot')
    ])
])


@app.callback(Output('plot', 'children'), Input('country-dropdown', 'value'))

def make_plot(value):
    figur = plot.fossil_share_elec(df, value)
    return dcc.Graph(id='plot-fig', figure=figur)

if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=True)
