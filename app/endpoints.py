import logging
import uuid
from fastapi import APIRouter, Depends, HTTPException, Query, status
from fastapi.security import OAuth2PasswordRequestForm
from app import cruds, models, schemas
from app.dependencies import get_db, get_settings, get_user_from_token
from app.hiboutik_api import HiboutikAPI, get_hiboutik_api
from app.utils import security
from app.utils.security import authenticate_user, create_access_token
from app.utils.settings import Settings
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter(
    tags=["clients"],
)

logger = logging.getLogger("logger")


@router.post(
    "/auth/simple_token",
    response_model=schemas.AccessToken,
    status_code=200,
)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db),
    settings: Settings = Depends(get_settings),
):
    """
    Ask for a JWT access token using oauth password flow.

    *username* and *password* must be provided

    Note: the request body needs to use **form-data** and not json.
    """
    user = await authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect login or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # We put the user id in the subject field of the token.
    # The subject `sub` is a JWT registered claim name, see https://datatracker.ietf.org/doc/html/rfc7519#section-4.1
    data = schemas.TokenData(sub=user.id, scopes="auth")
    access_token = create_access_token(settings=settings, data=data)
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me", response_model=schemas.User)
async def read_users_me(
    user: models.User = Depends(get_user_from_token),
):
    return user


@router.post("/users", response_model=schemas.User)
async def create_user(
    user: schemas.UserCreate,
    db: AsyncSession = Depends(get_db),
):
    user_db = models.User(
        id=uuid.uuid4(),
        username=user.username,
        email=user.email,
        password_hash=security.get_password_hash(user.password),
        is_active=True,
    )
    await cruds.create_user(db, user_db)
    return


####################################################################
#
#                             Clients
#
# Uncomment "user: models.User = Depends(get_user_from_token)" to add authentication
####################################################################


@router.get("/clients")
async def read_clients(
    hiboutik: HiboutikAPI = Depends(get_hiboutik_api),
    # user: models.User = Depends(get_user_from_token),
):
    return hiboutik.get("customers")


@router.get("/clients/search")
async def read_clients_with_filter(
    name: str = Query(None),
    hiboutik: HiboutikAPI = Depends(get_hiboutik_api),
    # user: models.User = Depends(get_user_from_token),
):
    return hiboutik.get("customers/search", params={"last_name": name})


@router.get("/clients/{client_id}")
async def read_client(
    client_id: str,
    hiboutik: HiboutikAPI = Depends(get_hiboutik_api),
    # user: models.User = Depends(get_user_from_token),
):
    return hiboutik.get(f"customer/{client_id}")


@router.get("/clients/{client_id}/sales")
async def read_client_sales(
    client_id: str,
    page: int = Query(1),
    hiboutik: HiboutikAPI = Depends(get_hiboutik_api),
    # user: models.User = Depends(get_user_from_token),
):
    sales = hiboutik.get(f"customer/{client_id}/sales")
    return sales[(page - 1) * 5 : min(page * 5, len(sales))]
