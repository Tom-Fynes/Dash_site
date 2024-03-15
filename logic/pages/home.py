import dash
from dash import html
import base64
import dash_bootstrap_components as dbc

from .blog_config.blog import article_cards

dash.register_page(__name__, path='/home')

encoded_image = base64.b64encode(open("logic/pages/assets/images/profile.jpg", 'rb').read())

jumbotron = html.Div(
    dbc.Container(
        [
            dbc.Container(
                [
                html.Img(src="data:image/png;base64,{}".format(encoded_image.decode()), className="rounded-circle avatar", style={
                    "margin-left": "auto",
                    "margin-right": "auto",
                    "box-shadow": "0 5px 15px rgba(126, 23, 142, 0.8)",
                    "border-radius": "50%"
                    }),
                ],
                class_name="center", style={"text-align": "center"}
            ),
            html.H3("Tom Fynes", style={"text-align": "center"}),
            html.P(
                "Software Engineer", style={"text-align": "center"}),
        ],
        fluid=True,
        className="py-3",
    ),
    className="p-3", style={"background-color": "transparent", "border": "none", "box-shadow": "none"},
)

blog = [
    dbc.Col(
        item,
        md=6,
        align='centre',
        style={"width": "25rem", "min-height": "18rem"}
    ) for item in article_cards[:3]
]

layout = html.Div(
    [  jumbotron,
        html.H4('Recent Posts', style={"text-align":"center", "padding":"10px"}),
        dbc.Container(
                [
        dbc.Row(
            blog,
            justify='centre',
            class_name='g-3'
        )
                ],
                fluid=True,
                className="py-3",
                class_name="center", style={"text-align": "center","padding":"10px"}
            ),
    ]
)
