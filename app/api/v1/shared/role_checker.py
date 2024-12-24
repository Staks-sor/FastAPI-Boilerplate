from typing import List

from starlette.requests import Request
from api.v1.user.models import RoleModel
from core.exceptions.base import ForbiddenException, UnauthorizedException


class CheckRole:
    def __init__(self, allowed_roles: List[str] = None, match_any: bool = True):
        if allowed_roles is None:
            allowed_roles = []
        self.allowed_roles = allowed_roles
        self.match_any = match_any

    async def __call__(self, request: Request):
        user = request.user
        if not user:
            raise UnauthorizedException

        roles: List[RoleModel] = user.roles
        if not roles:
            raise ForbiddenException

        role_names = [role.role for role in roles]

        if self.match_any:  # Если разрешена любая роль
            if any(role in self.allowed_roles for role in role_names):  # Пересечение
                return True
        else:  # Все роли пользователя должны быть в allowed_roles
            if all(role in self.allowed_roles for role in role_names):
                return True

        raise ForbiddenException