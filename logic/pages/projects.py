import dash
from dash import html

dash.register_page(__name__)

layout = html.Div([
    html.H1('Projects'),
    html.Div('This is our Archive page content.'),
])