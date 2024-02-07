from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession 

from .models import UserModel as UserMd
from .models import ChatModel as ChatMd
from .models import async_session


class User():
    def __init__(self, session):
        self.session: AsyncSession = session

    async def create(self, user_id: int, wca_id: str):
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


class Chat():
    def __init__(self, session):
        self.session: AsyncSession = session

    async def create(self, chat_id: int, lang: str = 'en'):
        async with self.session.begin():
            statement = select(ChatMd).where(ChatMd.chat_id == chat_id)
            resp = await self.session.execute(statement)
            chat = resp.scalar()
            
            if chat:
                statement = update(ChatMd).where(ChatMd.chat_id == chat_id).values(lang=lang)
                await self.session.execute(statement)
            else:
                chat = ChatMd(chat_id=chat_id, lang=lang)
                self.session.add(chat)
    
    async def get_lang(self, chat_id: int) -> ChatMd.lang:
        statement = select(ChatMd).where(ChatMd.chat_id == chat_id)
        chat = (await self.session.execute(statement)).scalar()
        await self.session.close()

        return chat.lang if chat else 'en'
    

async def user_db():
    async with async_session() as session:
        return User(session)


async def chat_db():
    async with async_session() as session:
        return Chat(session)
    