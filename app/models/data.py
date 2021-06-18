from typing import Optional

from app.models.core import IDModelMixin, CoreModel
from pydantic.class_validators import validator
from pydantic.types import Json


class DataRecord(IDModelMixin, CoreModel):
    """
    Any common logic to be shared by all models goes here.
    """
    endpoint: str
    data: Json
    links: Optional[Json]

    @validator('data', pre=True, allow_reuse=True)
    @validator('links', pre=True, allow_reuse=True)
    def decode_json(cls, v):
        return CoreModel.decode_json(cls, v)
