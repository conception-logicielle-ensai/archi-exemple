from fastapi import APIRouter, HTTPException

from dao.user_dao import UserDAO
from dto.user_dto import UserDTO
from services.user_service import UserService

user_router = APIRouter()


@user_router.post("/connect")
def connect(user_dto: UserDTO):
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