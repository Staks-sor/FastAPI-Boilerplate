from core.exceptions.base import CustomException
from core.enums.status_type import StatusType
from core.enums.exception_status import ExceptionStatus


class BaseException(CustomException):
    def __init__(self, exception_status: ExceptionStatus):
        """
        Базовый класс для всех пользовательских исключений.

        :param exception_status: Статус исключения, определённый в `ExceptionStatus`
        """
        self.status = StatusType.ERROR.value
        self.status_type = exception_status.name
        self.message = exception_status.message
        self._status_code = exception_status.status_code


class PasswordDoesNotMatchException(BaseException):
    def __init__(self):
        # Инициализация для "PasswordDoesNotMatchException"
        super().__init__(ExceptionStatus.PASSWORD_NOT_MATCHED)


class InvalidTokenException(BaseException):
    def __init__(self):
        # Инициализация для "InvalidTokenException"
        super().__init__(ExceptionStatus.INVALID_TOKEN)


class DecodeTokenException(BaseException):
    def __init__(self):
        # Инициализация для "DecodeTokenException"
        super().__init__(ExceptionStatus.UNPROCESSABLE_TOKEN)


class ExpiredTokenException(BaseException):
    def __init__(self):
        # Инициализация для "ExpiredTokenException"
        super().__init__(ExceptionStatus.TOKEN_EXPIRED)
