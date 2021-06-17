from pydantic import BaseModel


class BaseErrorModel(BaseModel):
    """
    Any common logic to be shared by all error models goes here.
    """
    error: str
    message: str


class AuthenticationError(BaseErrorModel):
    pass


class AuthorizationError(BaseErrorModel):
    pass


class BadRequestError(BaseModel):
    cause: str
    message: str


AuthorisationError = AuthorizationError


BaseResponses = {
    400: {"model": BadRequestError},
    401: {"model": AuthenticationError},
    403: {"model": AuthorizationError},
}
