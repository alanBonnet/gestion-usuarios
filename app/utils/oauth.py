from typing import Annotated
from fastapi import Depends, HTTPException, status
from app.utils.token import verificar_token

# OAuth
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth")


def obtener_sesion_usuario(token: Annotated[str, Depends(oauth2_scheme)]):
    """
    Retorna el contenido de un jwt a la ruta que use esta función
    en caso de que el token no exista o esté expirado también lanzará un
    HTTPException respectivo al caso.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token no válido.",
        headers={"WWW-Authenticate": "Bearer"},
    )
    # si se retorna verificar token, este dato se puede recibir en el endpoint/param "current_user"
    return verificar_token(token, credentials_exception)
