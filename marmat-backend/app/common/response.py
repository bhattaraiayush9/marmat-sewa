from datetime import datetime, timezone
from typing import Any, Generic, Optional, TypeVar
from uuid import uuid4

from pydantic import BaseModel

T = TypeVar("T")

class Meta(BaseModel):
    request_id: str
    timestamp: str
    tenant_id: Optional[str] = None
    pagination: Optional[dict] = None
    error_code: Optional[str] = None
    fields: Optional[dict] = None

class ApiResponse(BaseModel, Generic[T]):
    status: int
    message: str
    data: Optional[T] = None
    meta: Meta

def build_meta(**kwargs: Any)->Meta:
    return Meta(
        request_id=str(uuid4()),
        timestamp=datetime.now(timezone.utc).isoformat(),
        **kwargs
    )

def success(data: T, message: str = "Success", status_code: int = 200, **meta_kwargs)->ApiResponse[T]:
    return ApiResponse(status=status_code, message=message, data=data, meta=build_meta(**meta_kwargs))

def error(message: str, status_code: int, error_code: str, fields: dict|None = None)->ApiResponse[None]:
    return ApiResponse(status = status_code,message=message,data=None,meta=build_meta(error_code=error_code, fields=fields))
