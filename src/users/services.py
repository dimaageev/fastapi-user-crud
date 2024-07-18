from fastapi import HTTPException, status
from sqlmodel import Session, select

from .models import Employed, User, UserBase, UserBaseUpdate


async def get_user(user_id: int, session: Session) -> User:
    user = session.exec(select(User).where(User.id == user_id)).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'User with id:{user_id} not found',
        )
    return user


async def update_user(
    user_id: int, user_input: UserBaseUpdate, session: Session
) -> User:
    user = await get_user(user_id, session)

    if user_input.name:
        user.name = user_input.name

    if user_input.age:
        user.age = user_input.age

    if user_input.employed:
        user.employed = Employed(user_input.employed)

    session.add(user)
    session.commit()
    session.refresh(user)
    return user


async def delete_user(user_id: int, session: Session) -> str:
    user = await get_user(user_id, session)
    session.delete(user)
    session.commit()
    return f'User with id:{user_id} deleted'


async def create_user(user_input: UserBase, session: Session) -> User:
    user = User(
        name=user_input.name,
        age=user_input.age,
        employed=Employed(user_input.employed),
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
