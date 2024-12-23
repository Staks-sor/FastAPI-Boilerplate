from core.exceptions.base import CustomException
from core.enums.exception_status import ExceptionStatus
from core.enums.status_type import StatusType


class CustomStatusException(CustomException):
    def __init__(self, exception_status: ExceptionStatus):
        self.status = StatusType.ERROR.value
        self.status_type = exception_status.name
        self.message = exception_status.message
        self._status_code = exception_status.status_code


# Исключение для дублирования email
class DuplicateEmailException(CustomStatusException):
    def __init__(self):
        super().__init__(ExceptionStatus.DUPLICATE_EMAIL)


# Исключение для случая, когда пользователь не найден
class UserNotFoundException(CustomStatusException):
    def __init__(self):
        super().__init__(ExceptionStatus.USER_NOT_FOUND)
