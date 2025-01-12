from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession 

from .models import UserModel as UserMd
from .models import ChatModel as ChatMd


class DB:
    session: AsyncSession

    def __init__(self, session: AsyncSession):
        self.session = session


class Users(DB):
    '''This class is for managing the 'users' table'''
    async def create(self, user_id: int, wca_id: str):
        '''If chat exists, this method will update the user's wcaid
        Else it will create user in database'''
        statement = select(UserMd).where(UserMd.user_id == user_id)
        user = (await self.session.execute(statement)).scalar()
        
        if user:
            statement = update(UserMd).where(UserMd.user_id == user_id).values(wca_id=wca_id)
            await self.session.execute(statement)
        else:
            user = UserMd(user_id=user_id, wca_id=wca_id)
            self.session.add(user)
        
        await self.session.commit()
        await self.session.refresh(user)

    async def get(self, user_id: int) -> UserMd:
        """This method returns user"""
        statement = select(UserMd).where(UserMd.user_id == user_id)
        user = (await self.session.execute(statement)).scalar()

        return user


class Chats(DB):
    """This class is for managing the 'chats' table"""
    async def create(self, chat_id: int, lang: str = 'en'):
        """If chat exists, this method will update the chat's language
        Else it will create chat in database."""
        statement = select(ChatMd).where(ChatMd.chat_id == chat_id)
        resp = await self.session.execute(statement)
        chat = resp.scalar()
        
        if chat:
            statement = update(ChatMd).where(ChatMd.chat_id == chat_id).values(lang=lang)
            await self.session.execute(statement)
        else:
            chat = ChatMd(chat_id=chat_id, lang=lang)
            self.session.add(chat)
        
        await self.session.commit()
    
    async def get_lang(self, chat_id: int) -> str:
        """This method returns chat language, if chat doesn't exist return "en\""""
        statement = select(ChatMd).where(ChatMd.chat_id == chat_id)
        chat = (await self.session.execute(statement)).scalar()

        return chat.lang if chat else 'en'
