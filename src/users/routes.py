from collections.abc import Sequence

from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from src.db import get_session

from . import services
from .models import User, UserBase, UserBaseUpdate

router = APIRouter(prefix='/users', tags=['Users'])


@router.get('/')
async def read_users(
    session: Session = Depends(get_session),
) -> Sequence[User]:
    return session.exec(select(User)).all()


@router.post('/')
async def create_user(
    user_input: UserBase, session: Session = Depends(get_session)
) -> User:
    return await services.create_user(user_input, session)


@router.put('/{user_id}')
async def update_user(
    user_id: int,
    user_input: UserBaseUpdate,
    session: Session = Depends(get_session),
) -> User:
    return await services.update_user(user_id, user_input, session)


@router.delete('/{user_id}')
async def delete_user(
    user_id: int, session: Session = Depends(get_session)
) -> str:
    return await services.delete_user(user_id, session)


@router.get('/{user_id}')
async def get_user(
    user_id: int, session: Session = Depends(get_session)
) -> User:
    return await services.get_user(user_id, session)
