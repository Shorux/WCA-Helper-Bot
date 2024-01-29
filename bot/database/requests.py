from sqlalchemy import select, update

from bot.database.models import User, async_session


async def create_user(user: User) -> User:
    async with async_session() as session:
        session.add(user)
        await session.commit()
        await session.refresh(user)

    return user

async def get_user(user_id: int) -> User:
    async with async_session() as session:
        statement = select(User).where(User.user_id == user_id)
        user = (await session.execute(statement)).fetchone()

    return user

async def update_wca_id(user_id: int, wca_id: str) -> User:
    async with async_session() as session:
        statement = update(User).where(User.user_id == user_id).values(wca_id=wca_id)

        await session.execute(statement)
        await session.commit()

    return await get_user(user_id)