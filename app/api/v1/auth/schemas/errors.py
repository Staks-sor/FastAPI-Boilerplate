from core.enums.exception_status import ExceptionStatus
from core.enums.status_type import StatusType
from core.schemas.base import BaseAuthenticationError


class CustomAuthenticationError(BaseAuthenticationError):
    def __init__(self, exception_status: ExceptionStatus):
        """
        Базовый класс для всех ошибок аутентификации.

        :param exception_status: Статус ошибки, определённый в `ExceptionStatus`
        """
        self.status = StatusType.ERROR.value
        self.status_type = exception_status.name
        self.message = exception_status.message
        self._status_code = exception_status.status_code


class CustomUnauthorizedError(CustomAuthenticationError):
    def __init__(self):
        # Инициализация конкретной ошибки "Unauthorized"
        super().__init__(ExceptionStatus.UNAUTHORIZED)


class CustomInvalidTokenError(CustomAuthenticationError):
    def __init__(self):
        # Инициализация ошибки "Invalid Token"
        super().__init__(ExceptionStatus.INVALID_TOKEN)


class CustomDecodeTokenError(CustomAuthenticationError):
    def __init__(self):
        # Инициализация ошибки "Unprocessable Token"
        super().__init__(ExceptionStatus.UNPROCESSABLE_TOKEN)


class CustomExpiredTokenError(CustomAuthenticationError):
    def __init__(self):
        # Инициализация ошибки "Token Expired"
        super().__init__(ExceptionStatus.TOKEN_EXPIRED)

