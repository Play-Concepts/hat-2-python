from __future__ import annotations

from fastapi import APIRouter, Depends

from app.core.auth import get_current_user
from app.models.data import DataRecord
from app.models.responses import BaseResponses

router = APIRouter()
router.prefix = "/api/v2.6"


@router.get("/data/{num}", tags=["data"],
            responses=BaseResponses)
async def view_a(
    num: int,
    auth: Depends = Depends(get_current_user),
) -> DataRecord:

    data = {
        'data': num,
        "nested": {
            "hello": "world"
        }
    }

    data_record = DataRecord(
        endpoint="elyria/identity",
        data=data
    )
    return data_record
