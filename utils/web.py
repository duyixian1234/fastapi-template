from typing import Any, Generic, Optional, TypeVar

from pydantic.generics import GenericModel

DataT = TypeVar("DataT")


class BaseResponse(GenericModel, Generic[DataT]):
    success: bool = True
    code: int = 0
    msg: str = ""
    data: Optional[DataT]


def success_ret(data: Any = None) -> BaseResponse:
    return BaseResponse(data=data)


def failure_ret(code: int, message: str) -> BaseResponse:
    return BaseResponse(success=False, code=code, msg=message)
