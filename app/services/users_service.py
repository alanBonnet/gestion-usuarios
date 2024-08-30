from app.models.users import (
    Permissions,
    Rela_Role_Permissions,
    Roles,
    Users as Users_DB,
)
from fastapi import HTTPException, status
from app.schemas.users import PermisosEnumText, User, UpdateUsers
from sqlalchemy.orm import Session
import sqlalchemy as sa
from sqlalchemy import select, insert, update, delete, func

from app.utils.users_utils import get_list_permissions, have_permissions_to


def list(db: Session, current_user: str):
    this_user = (db.query(Users_DB).filter(Users_DB.username == current_user)).first()
    have_permissions_to(
        user=this_user, db=db, permissions=[PermisosEnumText.VER_USUARIOS]
    )
    users = db.query(Users_DB).filter(Users_DB.role_id > this_user.role_id).all()
    return users


def self_user(db: Session, current_user: str):
    this_user = (db.query(Users_DB).filter(Users_DB.username == current_user)).first()
    return {"usuario_actual": this_user}


def one(id: int, db: Session, current_user: str):
    this_user = (db.query(Users_DB).filter(Users_DB.username == current_user)).first()
    have_permissions_to(
        user=this_user, db=db, permissions=[PermisosEnumText.VER_USUARIOS]
    )

    user = (db.query(Users_DB).filter(Users_DB.id == id)).first()
    print({"user": user})
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado"
        )
    return {"usuario": user}


def create(body: User, db: Session, current_user: str):
    this_user = (db.query(Users_DB).filter(Users_DB.username == current_user)).first()
    have_permissions_to(
        user=this_user, db=db, permissions=[PermisosEnumText.CREAR_USUARIOS]
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
    nuevo_usuario = db.add(
        Users_DB(
            username=body.username,
            password=body.password,
            isActive=body.isActive,
            role_id=body.role_id.value,
        )
    )

    db.commit()
    new_user = db.query(Users_DB).filter(Users_DB.username == body.username).first()
    print(nuevo_usuario)
    return {"detail": "Usuario creado correctamente", "datos_usuario": new_user}


def update(id: int, body: UpdateUsers, db: Session, current_user: str):
    this_user = (db.query(Users_DB).filter(Users_DB.username == current_user)).first()
    have_permissions_to(
        user=this_user, db=db, permissions=[PermisosEnumText.ACTUALIZAR_USUARIOS]
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
