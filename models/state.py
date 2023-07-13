#!/usr/bin/python3
"""Defines the State class - inherits from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """Class represents a state.
    Attributes:
        name (str): The name of the state.
    """

    name = ""
