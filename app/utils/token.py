from typing import TypedDict
from fastapi import HTTPException, status
from jose import ExpiredSignatureError, JWTError, jwt
from datetime import datetime, timedelta
from app.core.config import settings
from pydantic import BaseModel

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM_HASH
ACCESS_TOKEN_EXPIRE_MINUTES = 1800


class TokenData(BaseModel):
    username: str


def create_access_token(data: dict):  # -> dict[str, int]:
    """
    Crea el token con la data que se le envíe
    la duración del mismo es de `1800 segundos`
    y devuelve un dict del siguiente formato:
    `{"token": str,"expires_in: int}`

    """
    to_encode = data.copy()
    print(to_encode)
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(claims=to_encode, key=SECRET_KEY, algorithm=ALGORITHM)
    return {"token": encoded_jwt, "expires_in": ACCESS_TOKEN_EXPIRE_MINUTES}


def verificar_token(token: str, credentials_exception) -> TokenData:
    """
    Verifica el token y retorna el contenido del mismo a la función que lo llame
    aplica validación de existencia y expiración
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_data: int = payload.get("sub")  # type: ignore
        if user_data is None:
            raise credentials_exception
        # este es el cuerpo de la salida que debe coincidir con el contenido de login
        return TokenData(username=user_data)
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Token expirado."
        )
    except JWTError as e:
        print(e)
        raise credentials_exception
