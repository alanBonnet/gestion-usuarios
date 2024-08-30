from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Annotated
from enum import Enum
from app.utils.types import NVARCHAR_16, NVARCHAR_50, NVARCHAR_100_NULLABLE


class PermisosEnum(Enum):
    VER_USUARIOS = 1
    CREAR_USUARIOS = 2
    ACTUALIZAR_USUARIOS = 3
    ELIMINAR_USUARIOS = 4
    VER_TAREAS = 5
    CREAR_TAREAS = 6
    ACTUALIZAR_TAREAS = 7
    ELIMINAR_TAREAS = 8


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


class Users(BaseModel):
    username: NVARCHAR_16
    password: NVARCHAR_16
    isActive: bool
    role_id: RolesEnum


class Tareas(BaseModel):
    titulo: NVARCHAR_50
    descripcion: NVARCHAR_100_NULLABLE


class UpdateUsers(BaseModel):
    password: NVARCHAR_16
    isActive: bool


class ShowUsers(BaseModel):
    pass

    class Config:
        from_attributes = True
