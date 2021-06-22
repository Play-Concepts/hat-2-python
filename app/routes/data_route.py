from __future__ import annotations

import uuid
from typing import List, Optional

from fastapi import APIRouter, Depends, status, Query

from app.core.auth import get_current_user
from app.models.data import DataRecord, DataRecordIn
from app.models.responses import BaseResponses, SuccessResponse

router = APIRouter()
router.prefix = "/api/v2.6"


@router.post("/data/{namespace}/{endpoint:path}", tags=["data"],
             responses=BaseResponses, status_code=status.HTTP_201_CREATED,
             summary="Create Data", operation_id="data_create")
async def create_data(namespace: str, endpoint: str, data: DataRecordIn,
                      auth: Depends = Depends(get_current_user)) -> DataRecord:

    data_record = DataRecord(
        recordId=uuid.uuid4(),
        namespace=namespace,
        endpoint=endpoint,
        data=data.json()
    )
    return data_record


@router.get("/data/{namespace}/{endpoint:path}", tags=["data"],
            responses=BaseResponses, status_code=status.HTTP_200_OK,
            summary="Read Data", operation_id="data_read")
async def read_data(namespace: str, endpoint: str,
                    auth: Depends = Depends(get_current_user)) -> List[DataRecord]:

    import json
    data = {
        'hello': 'world',
        'byebye': 'weirdness'
    }
    data_record = DataRecord(
        recordId=uuid.uuid4(),
        namespace=namespace,
        endpoint=endpoint,
        data=json.dumps(data)
    )

    data_record2 = DataRecord(
        recordId=uuid.uuid4(),
        namespace=namespace,
        endpoint=endpoint,
        data=json.dumps(data)
    )
    return [data_record, data_record2]


@router.delete("/data", tags=["data"],
               responses=BaseResponses, status_code=status.HTTP_200_OK,
               summary="Delete Data", operation_id="data_delete")
async def delete_data(records: Optional[List[uuid.UUID]] = Query(None),
                      auth: Depends = Depends(get_current_user)) -> SuccessResponse:
    print("records")
    print(records)
    return SuccessResponse(message="Records Deleted")


@router.put("/data", tags=["data"],
            responses=BaseResponses, status_code=status.HTTP_201_CREATED,
            summary="Update Data", operation_id="data_update")
async def update_data(data: List[DataRecord],
                      auth: Depends = Depends(get_current_user)) -> List[DataRecord]:
    return data
