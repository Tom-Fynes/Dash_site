import os
import base64
from pathlib import Path
from dash import html
import dash_bootstrap_components as dbc

from .constraints import Skills


class Cards:
    def __init__(self):
        self.skills = Skills

    def generate_card_list(self) -> list:

        results = []

        for skill in self.skills:
            card = self._get_skill_cards(skill.value)
            results.append(dbc.Col(html.Div(card), width=3))
        
        return results


    def _get_skill_cards(self, card_details: dict):

        image_path = self._get_image(card_details.get("image_name"))
        encoded_image = base64.b64encode(open(image_path, 'rb').read())

        card = dbc.Card(
        [
        dbc.CardImg(
            src="data:image/png;base64,{}".format(encoded_image.decode()), 
            top=True, 
            class_name="img-fluid",
            style= {
                "width":"15%", 
                "height=":"15%", 
                "display": "block", 
                "margin-left": "auto", 
                "margin-right": "auto", 
                "top":"10px",
                "position": "relative"
                },
            ),
        dbc.CardBody(
            [
                html.H4(card_details.get("title"), className="card-title"),
                html.P(
                    card_details.get("body"),
                    className="align-items-stretch col-md-10",
                )
                    ]
                ),
            ],
            style={"width": "25rem", "min-height": "18rem"},
        )
        return card
    
    def _get_image(self, image_name: str) -> str:
        parent = Path(__file__).resolve().parents[1] 
        image_path = os.path.join(parent, f"assets/images/{image_name}")

        return image_path

