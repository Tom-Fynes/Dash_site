import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.QUARTZ])


navbar = dbc.NavbarSimple(
    children=[
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem(f"{page['name']}", href=page["relative_path"])
                for page in dash.page_registry.values()
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="Dash Site",
    brand_href="#",
    color="primary",
    dark=True,
)


app.layout =  html.Div([ navbar,
    dash.page_container
])

if __name__ == '__main__':
    app.run(debug=True)