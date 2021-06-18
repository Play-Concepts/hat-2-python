import uuid
from typing import Optional

from pydantic import BaseModel
import json


class CoreModel(BaseModel):
    """
    Any common logic to be shared by all models goes here.
    """
    def decode_json(cls, v):
        if not isinstance(v, str):
            try:
                return json.dumps(v)
            except Exception as err:
                raise ValueError(f'Could not parse value into valid JSON: {err}')

        return v

    pass


class IDModelMixin(BaseModel):
    recordId: Optional[uuid.UUID]
