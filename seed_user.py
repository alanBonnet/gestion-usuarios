from sqlalchemy import create_engine, literal
from sqlalchemy.orm import sessionmaker
from app.db.database import Base
from app.models import Permissions, Roles, Users
from app.core.config import settings
from app.models.users import Rela_Role_Permissions


# Configuración de la base de datos
DATABASE_URL = settings.URL_DBs["Gestion_Usuarios"]
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()


def clear_existing_data():
    """Elimina todos los datos existentes en las tablas Users, Roles, Permissions, y rela_role_permissions"""
    session.query(Users).delete()
    session.query(Rela_Role_Permissions).delete()
    session.query(Roles).delete()
    session.query(Permissions).delete()
    session.commit()


def assign_permissions_to_roles(roles: list[Roles], permissions: list[Permissions]):
    """Asigna permisos específicos a cada rol"""
    # Permisos para ADMIN (todos los permisos)
    for permission in permissions:
        session.add(
            Rela_Role_Permissions(role_id=roles[0].id, permission_id=permission.id)
        )

    # Permisos para MODERADOR (todos menos ELIMINAR_USUARIOS)

    # Permisos para USUARIO (solo permisos relacionados con tareas)
    for permission in permissions:
        if permission.permission in [
            "VER_TAREAS",
            "CREAR_TAREAS",
            "ACTUALIZAR_TAREAS",
            "ELIMINAR_TAREAS",
        ]:
            session.add(
                Rela_Role_Permissions(
                    role_id=roles[2].id,
                    permission_id=permission.id,
                )
            )

    session.commit()


def create_default_roles_and_permissions() -> tuple[Roles, list[Permissions]]:
    # Crear roles
    l_roles = ["ADMIN", "MODERADOR", "USUARIO"]
    # Crear permisos
    l_permissions = [
        "VER_USUARIOS",
        "CREAR_USUARIOS",
        "ACTUALIZAR_USUARIOS",
        "ELIMINAR_USUARIOS",
        "VER_TAREAS",
        "CREAR_TAREAS",
        "ACTUALIZAR_TAREAS",
        "ELIMINAR_TAREAS",
    ]
    permissions_db = [
        Permissions(permission=permission) for permission in l_permissions
    ]
    roles = [Roles(role=role) for role in l_roles]

    for role in roles:
        session.add(role)

    # TODO: incorporar los permisos a cada role
    for permission in permissions_db:
        session.add(permission)
    session.commit()
    assign_permissions_to_roles(roles, permissions_db)

    return roles[0], permissions_db


def create_admin_user(admin_role, permissions):
    # Crear un usuario administrador

    admin_user = Users(
        username="admin",
        password="admin",
        role_id=admin_role.id,
        isActive=True,
    )
    session.add(admin_user)

    session.commit()


def main():
    clear_existing_data()
    # Crear roles y permisos
    admin_role, permissions = create_default_roles_and_permissions()

    # Crear usuario administrador
    create_admin_user(admin_role, permissions)

    print("Datos iniciales cargados con éxito.")


if __name__ == "__main__":
    main()
