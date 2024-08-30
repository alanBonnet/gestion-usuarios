from app.models.users import (
    Permissions,
    Rela_Role_Permissions,
    Roles,
    Users as Users_DB,
)
from fastapi import HTTPException, status
from app.schemas.users import PermisosEnumText, Users, UpdateUsers
from sqlalchemy.orm import Session
import sqlalchemy as sa
from sqlalchemy import select, insert, update, delete, func

from app.utils.users_utils import get_list_permissions, have_permissions_to


def list(db: Session, current_user: str):
    this_user = (db.query(Users_DB).filter(Users_DB.username == current_user)).first()
    have_permissions_to(
        user=this_user, db=db, permissions=[PermisosEnumText.VER_USUARIOS]
    )
    users = db.query(Users_DB).all()
    return users


def self_user(db: Session, current_user: str):
    this_user = (db.query(Users_DB).filter(Users_DB.username == current_user)).first()

    return {"usuario_actual": this_user}


def one(id: int, db: Session, current_user: str):
    this_user = (db.query(Users_DB).filter(Users_DB.username == current_user)).first()
    if not (this_user.role_id in [1, 2]):

        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Acceso restringido"
        )
    user = db.query(Users_DB).filter(Users_DB.id == id)
    return {"usuario": user}


def create(body: Users, db: Session, current_user: str):
    this_user = (db.query(Users_DB).filter(Users_DB.username == current_user)).first()
    if not (this_user.role_id in [1, 2]):

        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Acceso restringido"
        )
    l_existUsers = db.query(Users_DB).all()
    existUsers_verif = [
        existUser for existUser in l_existUsers if existUser.username == body.username
    ]
    if len(existUsers_verif):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ya existe un usuario con ese username",
        )
    nuevo_usuario = insert(Users_DB).values(
        {
            "username": body.username,
            "password": body.password,
            "isActive": body.isActive,
            "role_id": body.role_id.value,
        }
    )
    db.execute(nuevo_usuario)
    db.commit()
    print(nuevo_usuario)
    return {"detail": "Usuario creado correctamente"}


def update(id: int, body: UpdateUsers, db: Session, current_user: str):
    this_user = (db.query(Users_DB).filter(Users_DB.username == current_user)).first()
    if not (this_user.role_id in [1, 2]):

        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Acceso restringido"
        )
    nuevo_usuario = db.query(Users_DB).filter(Users_DB.id == int(id))
    nuevo_usuario.update(
        {
            "password": Users_DB.set_password(
                self=nuevo_usuario, password=body.password
            ),
        }
    )
    db.commit()
    print("USUARIASO", body.password, id)
    return id


def delete(id: int, db: Session):
    pass
