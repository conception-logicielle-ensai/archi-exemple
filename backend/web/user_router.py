from fastapi import APIRouter, HTTPException

from dto.user_dto import UserConnectDTO, UserCreateDTO
from services.exceptions.user_exeptions import UserAlreadyExistsError
from services.user_service import UserService


user_router = APIRouter(prefix="/users", tags=["users"])


@user_router.post("/connect")
def connect(user_dto: UserConnectDTO):
    """
    Endpoint qui utilise la méthode `peut_se_connecter` pour vérifier si l'utilisateur peut accéder.
    Un utilisateur avec le rôle "admin" est nécessaire.
    """
    user_service = UserService.of_context()
    try:
        user = user_service.get_user(user_dto=user_dto)
        return (
            {"message": f"User {user.username} can connect as admin."}
            if user_service.peut_se_connecter(user=user)
            else {"message": f"User {user.username} cannotconnect as admin."}
        )
    except ValueError as e:
        raise HTTPException(404, str(e)) from e


@user_router.get("/")
def get_users():
    user_service = UserService.of_context()
    return user_service.get_users()


@user_router.post("/")
def create_user(user: UserCreateDTO):
    user_service = UserService.of_context()
    try:
        return user_service.save_user(user)
    except UserAlreadyExistsError:
        raise HTTPException(
            status_code=409, detail="Le nom d'utilisateur existe déjà"
        ) from None
