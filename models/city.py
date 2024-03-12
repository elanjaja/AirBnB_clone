#!/usr/bin/python3
"""City module"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class:
        state_id(str): it will be the State.id
        name(str): the of the city
    """
    state_id = ""
    name = ""
