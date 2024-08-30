from fastapi import HTTPException, status
from app.models.users import Users as Users_DB

from app.utils.token import create_access_token
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from passlib.context import CryptContext


def login(auth: OAuth2PasswordRequestForm, db: Session):
    user = db.query(Users_DB).filter(Users_DB.username == auth.username).first()

    if user is None:
        raise HTTPException(
            detail="el usuario no existe",
            status_code=status.HTTP_400_BAD_REQUEST,
        )
    same_password = Users_DB.verify_password(user, auth.password)  # type: ignore
    # # se crea el token con el username y role
    if not same_password:
        raise HTTPException(
            detail="Usuario o contraseña incorrectos",
            status_code=status.HTTP_400_BAD_REQUEST,
        )
    access_token = create_access_token(
        data={"sub": user.username},
    )
    return {
        "access_token": access_token["token"],
        "expires_in": access_token["expires_in"],
        "token_type": "bearer",
    }
