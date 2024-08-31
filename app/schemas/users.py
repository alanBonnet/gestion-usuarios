from datetime import datetime
from pydantic import BaseModel, Field
from typing import Annotated
from enum import Enum
from app.utils.types import NVARCHAR_16, NVARCHAR_50, NVARCHAR_100_NULLABLE


class PermisosEnumText(Enum):
    VER_USUARIOS = "VER_USUARIOS"
    CREAR_USUARIOS = "CREAR_USUARIOS"
    ACTUALIZAR_USUARIOS = "ACTUALIZAR_USUARIOS"
    ELIMINAR_USUARIOS = "ELIMINAR_USUARIOS"
    VER_TAREAS = "VER_TAREAS"
    CREAR_TAREAS = "CREAR_TAREAS"
    ACTUALIZAR_TAREAS = "ACTUALIZAR_TAREAS"
    ELIMINAR_TAREAS = "ELIMINAR_TAREAS"


class RolesEnum(Enum):
    ADMIN = 1
    MODERADOR = 2
    USER = 3


class User(BaseModel):
    username: NVARCHAR_16
    isActive: bool
    role_id: RolesEnum


class CreateUser(User):
    password: NVARCHAR_16

    class Config:
        from_attributes = True


class Permission(BaseModel):
    permission: str
    id: int


class Role(BaseModel):
    id: int
    role: str
    permissions: list[Permission]


class UserExtendido(User):
    createdAt: datetime
    updatedAt: datetime
    role: Role

    class Config:
        from_attributes = True


class Tareas(BaseModel):
    titulo: NVARCHAR_50
    descripcion: NVARCHAR_100_NULLABLE


class UpdateUsers(BaseModel):
    password: NVARCHAR_16
    isActive: bool


class ShowSelfUser(BaseModel):
    usuario_actual: User


class ShowUsers(BaseModel):
    usuarios_list: list[UserExtendido]

    # class Config:
    #     from_attributes = True
