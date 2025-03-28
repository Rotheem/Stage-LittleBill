from datetime import datetime
import uuid
from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class User(BaseModel):
    id: uuid.UUID
    username: str
    email: str
    is_active: bool = True


class AccessToken(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    sub: uuid.UUID  # Subject: the user id
    iss: str | None = None
    aud: str | None = None
    cid: str | None = None  # The client_id of the service which receives the token
    iat: datetime | None = None
    nonce: str | None = None
    scopes: str = ""
    # exp and iat elements are added by the token generation function
