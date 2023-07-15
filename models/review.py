#!/usr/bin/python3
""" Class review """

from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review- inherits from base model.
    Attributes:
        place_id (str): The Place id i.e place.id.
        user_id (str): The User id i.e user.id.
        text (str): The review text.
    """

    place_id = ""
    user_id = ""
    text = ""
