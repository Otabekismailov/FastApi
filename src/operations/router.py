import typing
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from .models import operation
from .schemas import OperationCreate, OperationRead

router = APIRouter(
    prefix="/operations",
    tags=["Operation"]
)


# @router.get("/", response_model=OperationRead)
# async def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
#     query = select(operation).where(operation.c.type == operation_type)
#     result = await session.execute(query)
#     for item in result.all():
#         data = OperationRead(id=item.id, quantity=item.quantity, figi=item.figi,
#                              instrument_type=item.instrument_type,
#                              date=item.date, type=item.type, )
#         return data


@router.get("/notes/", response_model=List[OperationRead | None])
async def read_notes(pk: int, session: AsyncSession = Depends(get_async_session)):
    query = select(operation).where(operation.c.id == pk)
    # query = operation.select().where(operation.c.id == pk)
    result = await session.execute(query)
    return result.all()
    # if result:
    #     if result.all() is not None:
    #         print(result.all())
    #         return result.all()
    #     raise HTTPException(status_code=404, detail="No Expenses found")

    # return result.all()
    # if result.all() is not None:
    #     return {"data": result.scalar_one_or_none()}
    # return HTTPException(status_code=404, detail="Nope! I don't like 3.")


@router.post("post/")
async def add_specific_operations(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(operation).values(**new_operation.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": stmt}
