from ctypes import Union
from datetime import datetime
from typing import Any
from pydantic import BaseModel, ConfigDict


class Login(BaseModel):
    username: str
    password: str


# class AccessToken(BaseModel):
# access_token: str
# expires_in: int
# token_type: str


class ShowLogin(BaseModel):
    access_token: str
    expires_in: int
    token_type: str

    class Config(ConfigDict):
        from_attributes = True
