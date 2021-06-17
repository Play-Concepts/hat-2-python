from __future__ import annotations

from fastapi import APIRouter, Depends
from typing import Dict

from app.core.auth import get_current_user
from app.models.responses import BaseResponses

router = APIRouter()


@router.get("/api_a/{num}", tags=["data"],
            responses=BaseResponses)
async def view_a(
    num: int,
    auth: Depends = Depends(get_current_user),
) -> Dict[str, int]:

    data = {
        'data': num
    }
    return data
