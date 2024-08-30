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
    permis = (
        select(
            Users_DB, Roles, func.array_agg(Permissions.permission).label("Permissions")
        )
        .where(
            Users_DB.id == user.id
            and Users_DB.role_id == Roles.id
            and Rela_Role_Permissions.permission_id == Permissions.id
        )
        .group_by(Users_DB.id, Roles.id)
    )
    r = db.execute(permis).first()
    print(r)
    print(user.id)
    print(
        {
            "prueba": (
                Users_DB.id == user.id
                and Users_DB.role_id == Roles.id
                and Rela_Role_Permissions.permission_id == Permissions.id
            ).__dict__
        }
    )
    # return ListPermissionsUser(
    #     user=r[0]._asdict()["Users"].username, has_permissions=r[0][1]
    # )


def have_permissions_to(
    user: Users_DB, db: Session, permissions: list[PermisosEnumText]
):
    permissions_user = get_list_permissions(user, db)
    print({"enum_de_permisos": permissions})
    # print({"permisos_del_usuario": permissions_user.has_permissions})
    for p in permissions:
        # if p.value in permissions_user.has_permissions:
        print("SI TIENE")
    # print([row._asdict() for row in r])
