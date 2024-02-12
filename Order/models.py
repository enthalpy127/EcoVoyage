import flask
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
from flask import Flask
# Incorporate data
df = pd.read_csv('order_data_export.csv')

# Initialize the app
app_flask = flask.Flask(__name__)

app = Dash(__name__, server=app_flask, url_base_pathname='/plotly/')

# App layout
app.layout = html.Div([
    html.Div(children='My First App with Data'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10),
    dcc.Graph(figure={}, id="controls-and-graph"),
    dcc.RadioItems(options=['sum', 'avg'], value='sum', id='controls-and-radio-item-x'),
    dcc.RadioItems(options=['Number of Adults', 'Number of Children', 'total_amount', 'Refunded'], value='Number of Adults', id='controls-and-radio-item-y'),
])

@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='controls-and-radio-item-y', component_property='value'),
    Input(component_id='controls-and-radio-item-x', component_property='value')
)
def update_graph(col_chosen, fuc_chosen):
    fig = px.histogram(df, x='destination', y=col_chosen, histfunc=fuc_chosen)
    return fig



@app_flask.route('/plotly_dashboard')
def render_dashboard():
    return flask.redirect('/plotly/')

# Run the apps
if __name__ == '__main__':
    app.run(debug=True)