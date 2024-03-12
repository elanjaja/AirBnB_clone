#!/usr/bin/python3
"""
This class helps create a user
The User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """USER CLASS DETAILS """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
