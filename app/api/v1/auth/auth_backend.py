from typing import Sequence, Tuple, Union

from starlette.requests import HTTPConnection
from fastapi.security.utils import get_authorization_scheme_param
from starlette.authentication import (
    AuthenticationBackend,
    AuthenticationError,
    UnauthenticatedUser,
)

from api.v1.auth.schemas.errors import (
    CustomUnauthorizedError,
    CustomDecodeTokenError,
    CustomInvalidTokenError,
    CustomExpiredTokenError,
)
from api.v1.auth.schemas.exceptions import DecodeTokenException, ExpiredTokenException
from api.v1.auth.service import AuthService
from api.v1.user.schemas.responses import SystemUser


from typing import Tuple, Union, Sequence
from starlette.authentication import AuthenticationBackend, HTTPConnection
from core.exceptions import CustomUnauthorizedError, CustomDecodeTokenError, CustomExpiredTokenError, CustomInvalidTokenError
from core.services.auth import AuthService
from core.models import SystemUser, UnauthenticatedUser
from core.utils import get_authorization_scheme_param


class AuthBackend(AuthenticationBackend):
    def __init__(
            self,
            prefix: str,
            exclude_paths: Sequence[str] = [],
            auth_service: AuthService = AuthService()
    ):
        """
        Инициализирует класс аутентификации.
        :param prefix: Префикс для URL
        :param exclude_paths: Пути, исключенные из аутентификации
        :param auth_service: Экземпляр сервиса аутентификации
        """
        self.prefix = prefix
        self.exclude_paths = exclude_paths
        self.auth_service = auth_service

    async def authenticate(
            self,
            conn: HTTPConnection,
    ) -> Tuple[bool, Union[SystemUser, UnauthenticatedUser]]:
        """
        Проверка аутентификации по токену.
        :param conn: HTTP соединение
        :return: Tuple с результатом аутентификации и пользователем
        """
        current_path = conn.url.path.lstrip(self.prefix)

        # Пропустить пути, которые исключены из аутентификации
        if any(current_path.startswith(path) for path in self.exclude_paths):
            return False, UnauthenticatedUser()

        # Извлечение и проверка токена авторизации
        authorization: str = conn.headers.get("Authorization")
        if not authorization:
            raise CustomUnauthorizedError

        scheme, token = get_authorization_scheme_param(authorization)

        # Проверка схемы токена
        if scheme.lower() != "bearer" or not token:
            raise CustomUnauthorizedError

        # Обработка токена
        try:
            user = await self.auth_service.get_user_from_access_token(token)
            conn.scope["user"] = user
        except DecodeTokenException:
            raise CustomDecodeTokenError
        except ExpiredTokenException:
            raise CustomExpiredTokenError
        except Exception as e:
            # Логируем или выводим исключение перед возникновением ошибки.
            raise CustomInvalidTokenError

        return True, user
