from fastapi import APIRouter

from utils.web import BaseResponse, success_ret

common_route = APIRouter(prefix="/common")


@common_route.get("/status", response_model=BaseResponse)
async def status() -> BaseResponse:
    return success_ret(data={"status": "服务正常"})
