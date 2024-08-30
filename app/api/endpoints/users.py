from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
from app.schemas.users import ShowSelfUser, User, ShowUsers, UpdateUsers, UserExtendido
from app.services import users_service
from app.db.database import get_db_P0
from app.utils.oauth import obtener_sesion_usuario
from app.utils.token import TokenData

router = APIRouter()


@router.get("/me", response_model=ShowSelfUser)
def obtener_mis_datos(
    db: Session = Depends(get_db_P0),
    current_user: TokenData = Depends(obtener_sesion_usuario),
):
    self_user = users_service.self_user(db=db, current_user=current_user.username)
    return self_user


@router.get("/", response_model=list[UserExtendido])
def obtener_users_listado(
    db: Session = Depends(get_db_P0),
    current_user: TokenData = Depends(obtener_sesion_usuario),
):
    users_list = users_service.list(db=db, current_user=current_user.username)
    return users_list


@router.get("/{users_id}")
def obtener_un_user(
    users_id: int,
    db: Session = Depends(get_db_P0),
    current_user: TokenData = Depends(obtener_sesion_usuario),
):
    users_one = users_service.one(
        id=users_id, db=db, current_user=current_user.username
    )
    print(users_one)
    return users_one


@router.post(
    "/",
    #  response_model=ShowUsers
)
def registrar_users(
    users: User,
    db: Session = Depends(get_db_P0),
    current_user: TokenData = Depends(obtener_sesion_usuario),
):
    users_create = users_service.create(
        body=users, db=db, current_user=current_user.username
    )
    return users_create


@router.patch(
    "/{users_id}",
    #   response_model=ShowUsers
)
def editar_users(
    user_id: int,
    users: UpdateUsers,
    db: Session = Depends(get_db_P0),
    current_user: TokenData = Depends(obtener_sesion_usuario),
):
    users_update = users_service.update(
        body=users, id=user_id, db=db, current_user=current_user.username
    )
    return users_update


@router.delete("/{users_id}", response_model=ShowUsers)
def eliminar_users(users_id: int, db: Session = Depends(get_db_P0)):
    users_delete = users_service.delete(id=users_id, db=db)
    return users_delete
