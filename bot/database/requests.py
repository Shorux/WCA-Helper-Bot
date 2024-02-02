from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession 

from bot.database.models import User as UserMd
from bot.database.models import async_session

class User():
    def __init__(self, session):
        self.session: AsyncSession = session

    async def create(self, user: UserMd) -> UserMd:
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)

        return user


    async def get(self, user_id: int) -> UserMd:
        statement = select(UserMd).where(UserMd.user_id == user_id)
        user = (await self.session.execute(statement)).scalar()

        return user


    async def update_wca_id(self, user_id: int, wca_id: str) -> None:
        statement = update(UserMd).where(UserMd.user_id == user_id).values(wca_id=wca_id)

        await self.session.execute(statement)
        # await self.session.commit()

async def DB() -> User:
    async with async_session() as session:
        return User(session)
    