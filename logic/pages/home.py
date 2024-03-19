import dash
from dash import html
import base64
import dash_bootstrap_components as dbc

from .blog_config.blog import article_cards

dash.register_page(__name__, path='/home',order=1)

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

emis_link = html.A("EMIS Group plc", "https://www.emishealth.com/")

about = html.Div([
    dbc.Container(
        [
        html.H3("About Me", style={"text-align": "center"}),
        html.P("Hi, I'm Tom"),
        html.A("EMIS Group plc", "https://www.emishealth.com/"),
        html.P(f"""I am a passionte Software Engineer currently working as a Senior Data Engineer at 
                {emis_link}. 
                within their Data and Analytics department, 
                with a background in data engineering, analytics, and leadership, 
                I am highly passionate about analytics and the insights 
                and benefits data driven solutions can bring.""")
        ],
        style={"padding":"10px", "margin":"auto", "width":"50%"},),
    ],
    className="p-3",
)


blog = [
    dbc.Col(
        item,
        md=6,
        align='centre',
        style={"width": "25rem", "min-height": "18rem"}
    ) for item in article_cards[:4]
]

layout = html.Div(
    [  jumbotron,
        dbc.Row(
            about,
            justify='centre',
            class_name='g-3',
        ),
        html.H4('Recent Posts', style={"text-align":"center"}),
        dbc.Row(
            blog,
            justify='centre',
            class_name='g-3',
            style={"text-align": "center","padding":"10px", "margin":"auto", "width":"50%"}
        )
    ]
)
