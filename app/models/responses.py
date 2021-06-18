from typing import Union

from pydantic import BaseModel
from pydantic.types import Json


class BaseErrorModel(BaseModel):
    """
    Any common logic to be shared by all error models goes here.
    """
    error: str
    message: Union[str, Json]


class AuthenticationError(BaseErrorModel):
    pass


class AuthorizationError(BaseErrorModel):
    pass


class NotFoundError(BaseErrorModel):
    pass


class BadRequestError(BaseModel):
    cause: str
    message: Union[str, Json]


AuthorisationError = AuthorizationError


BaseResponses = {
    400: {"model": BadRequestError},
    401: {"model": AuthenticationError},
    403: {"model": AuthorizationError},
    404: {"model": NotFoundError}
}
