from core.schemas.base import BaseResponse
from core.enums.response_status import ResponseStatus
from core.enums.status_type import StatusType


class BaseUserResponse(BaseResponse):
    status: str
    status_type: str
    message: str
    _status_code: int

    def __init__(self, status_type: str, status_code: int, message: str):
        self.status = StatusType.SUCCESS.value if status_code == 200 else StatusType.ERROR.value
        self.status_type = status_type
        self.message = message
        self._status_code = status_code


class UserRegisteredSuccessfully(BaseUserResponse):
    def __init__(self):
        super().__init__(
            status_type=ResponseStatus.USER_REGISTERED.name,
            status_code=ResponseStatus.USER_REGISTERED.status_code,
            message=ResponseStatus.USER_REGISTERED.message
        )


class UserNotFound(BaseUserResponse):
    def __init__(self):
        super().__init__(
            status_type=ResponseStatus.USER_NOT_FOUND.name,
            status_code=ResponseStatus.USER_NOT_FOUND.status_code,
            message=ResponseStatus.USER_NOT_FOUND.message
        )


class DuplicateEmail(BaseUserResponse):
    def __init__(self):
        super().__init__(
            status_type=ResponseStatus.DUPLICATE_EMAIL.name,
            status_code=ResponseStatus.DUPLICATE_EMAIL.status_code,
            message=ResponseStatus.DUPLICATE_EMAIL.message
        )

