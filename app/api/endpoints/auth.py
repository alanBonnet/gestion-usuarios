from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.db.database import get_db_P0
from app.schemas.auth import ShowLogin
from app.services import auth_service
from sqlalchemy.orm import Session

router = APIRouter()


@router.post(
    "/",
    # response_model=ShowLogin
)
def login(
    auth: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db_P0),
):

    login_create = auth_service.login(auth=auth, db=db)
    return login_create
