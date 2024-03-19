import dash
import more_itertools as mit
from dash import html
import dash_bootstrap_components as dbc

from .layouts import Cards

dash.register_page(__name__,order=4)

cards = Cards().generate_card_list()
sections = list(mit.chunked(cards,3))

def get_skill_layout(sections: list):

    results = []

    for section in sections:
        results.append(dbc.Row(
                    section,
                    justify="center"
                ))
        results.append(dbc.Row(dbc.Col(html.Br())))

    return results

layout = html.Div([
    html.H1('skills', style={"text-align":"center", "padding":"10px"}),
    html.Div(
    get_skill_layout(sections)
    )
])
