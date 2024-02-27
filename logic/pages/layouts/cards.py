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

        card = dbc.Card(
        [
        dbc.CardImg(src=card_details.get("image_path"), top=True),
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
