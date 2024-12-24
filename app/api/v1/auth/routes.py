from fastapi import APIRouter
from api.v1.auth.schemas.responses import TokenResponse
from api.v1.auth.view import AuthView
from api.v1.register.schemas.responses import UserNotFound
from api.v1.shared.schemas.responses import ValidationErrorResponse

auth_views = AuthView()

auth_router = APIRouter(
    responses={
        404: {"description": "Not found", "model": UserNotFound},
        422: {"description": "Validation Error", "model": ValidationErrorResponse},
    },
)


# Функция для добавления общих маршрутов
def add_token_route(router: APIRouter, path: str, method: str, name: str):
    router.add_api_route(
        path,
        getattr(auth_views, method),
        methods=["POST"],
        description=f"{name} - User Authentication and create access token",
        name=f"Authentication-{name}",
        response_model_by_alias=False,
        response_model=TokenResponse,
    )


# Добавляем маршруты для получения токена и обновления токена с помощью функции
add_token_route(auth_router, "/token", "access", "AccessToken")
add_token_route(auth_router, "/token/refresh", "refresh", "AccessToken-From-RefreshToken")
