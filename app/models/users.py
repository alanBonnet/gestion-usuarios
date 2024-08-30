from sqlalchemy import (
    ARRAY,
    Column,
    String,
    Integer,
    DateTime,
    Boolean,
    ForeignKey,
    event,
)
from sqlalchemy.orm import relationship
from datetime import datetime
from passlib.context import CryptContext
from app.db.database import Base


""" 
    Si practicamente olvidé que necesariamente
    tenía que usar el backpopulates para ayudar 
    en el desarrollo de la api pero en base de 
    datos con el ForeignKey ya es suficiente,
    cómo ayuda me diran? pues al consultar un usuario
    por ejemplo: sin el backpopulates si queremos 
    traer el usuario con el rol que tiene debería 
    traerse también el rol con el filtro que sea el que 
    tiene el usuario y con backpopulates no es necesario 
    ese procedimiento con solo traer el usuario ya tiene 
    el rol relacionado 
"""


# tabla intermedia para relacionar roles y permisos (muchos a muchos)
class Rela_Role_Permissions(Base):
    __tablename__ = "rela_role_permissions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    role_id = Column(Integer, ForeignKey("Roles.id"), primary_key=True, nullable=True)
    permission_id = Column(
        Integer, ForeignKey("Permissions.id"), primary_key=True, nullable=True
    )


class Permissions(Base):
    __tablename__ = "Permissions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    permission = Column(String, nullable=False)

    # relación inversa para los roles
    roles = relationship(
        "Roles",
        secondary=Rela_Role_Permissions.__tablename__,
        back_populates="permissions",
    )


class Roles(Base):
    __tablename__ = "Roles"
    id = Column(Integer, primary_key=True, autoincrement=True)
    role = Column(String, nullable=False)
    # relación con permisos
    permissions = relationship(
        "Permissions",
        secondary=Rela_Role_Permissions.__tablename__,
        back_populates="roles",
    )

    # relación inversa para los usuarios
    users = relationship("Users", back_populates="role")


pwd_context = CryptContext(schemes=["argon2"])


class Users(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    role_id = Column(Integer, ForeignKey("Roles.id"))
    isActive = Column(Boolean, default=True)
    createdAt = Column(DateTime, default=datetime.now())
    updatedAt = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

    # relación con roles
    role = relationship("Roles", back_populates="users")

    def set_password(self, password: str):
        self.password = pwd_context.hash(password)
        return self.password

    def verify_password(self, password: str) -> bool:

        return pwd_context.verify(password, self.password)  # type: ignore


# def hash_password_before_insert(mapper, connection, target):
#     if target.password:

#         target.password = pwd_context.hash(target.password)


# # función para hashear la contraseña antes de actualizar
# def hash_password_before_update(mapper, connection, target):
#     # fe asegura de que la contraseña no se hashee nuevamente si no ha cambiado
#     state = target._sa_instance_state
#     hist = state.attrs.password.history
#     if hist.has_changes() and target.password:
#         target.password = pwd_context.hash(target.password)


# # asociar las funciones de evento con las operaciones before_insert y before_update
# event.listen(target=Users, identifier="before_insert", fn=hash_password_before_insert)
# event.listen(Users, "before_update", hash_password_before_update)
