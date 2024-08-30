from fastapi import HTTPException, status
from pydantic import BaseModel
from sqlalchemy import func, select
from app.models.users import (
    Permissions,
    Rela_Role_Permissions,
    Roles,
    Users as Users_DB,
)
from sqlalchemy.orm import Session

from app.schemas.users import PermisosEnumText


class ListPermissionsUser(BaseModel):
    user: str
    has_permissions: list[str]


def get_list_permissions(user: Users_DB, db: Session) -> ListPermissionsUser:
    user_data = db.query(Users_DB).filter(Users_DB.username == user.username).first()
    permissions_user = [
        perm_user.permission for perm_user in user_data.role.permissions
    ]
    return permissions_user


def have_permissions_to(
    user: Users_DB, db: Session, permissions: list[PermisosEnumText]
):
    permissions_user = get_list_permissions(user, db)
    if len(permissions) == 1:
        if permissions[0].value not in permissions_user:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="No tiene permisos"
            )
        return permissions[0] in permissions_user
