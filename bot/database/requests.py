from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession 

from .models import UserModel as UserMd
from .models import async_session


class User():
    def __init__(self, session):
        self.session: AsyncSession = session

    async def create(self, user_id: int, wca_id: str) -> UserMd:
        async with self.session.begin():
            statement = select(UserMd).where(UserMd.user_id == user_id)
            user = (await self.session.execute(statement)).scalar()
            
            if user:
                statement = update(UserMd).where(UserMd.user_id == user_id).values(wca_id=wca_id)
                await self.session.execute(statement)
            else:
                user = UserMd(user_id=user_id, wca_id=wca_id)
                self.session.add(user)

    async def get(self, user_id: int) -> UserMd:
        statement = select(UserMd).where(UserMd.user_id == user_id)
        user = (await self.session.execute(statement)).scalar()
        await self.session.close()

        return user

    
async def DB():
    async with async_session() as session:
        return User(session)
