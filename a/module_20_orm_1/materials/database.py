from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String,create_engine

engine = create_engine("sqlite:///python.db",echo=True)

class Base(DeclarativeBase):
	pass


class UserBase(Base):
    __tablename__ = 'users'

    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(String(30))

Base.metadata.create_all(engine)