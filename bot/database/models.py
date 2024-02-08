from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

from config import SQLALCHEMY_URL


engine = create_async_engine(SQLALCHEMY_URL)
async_session = async_sessionmaker(engine, autoflush=False, autocommit=False)


class Base(AsyncAttrs, DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)


class UserModel(Base):
    __tablename__ = 'users'

    user_id = mapped_column(BigInteger, unique=True)
    wca_id: Mapped[str] = mapped_column()

    def __repr__(self):
        return f'User<{self.user_id}>'


class ChatModel(Base):
    __tablename__ = 'chats'

    chat_id = mapped_column(BigInteger, unique=True)
    lang: Mapped[str] = mapped_column(default='en')

    def __repr__(self):
        return f'User<{self.chat_id}>'


async def init_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
