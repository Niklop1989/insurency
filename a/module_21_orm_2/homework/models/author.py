from sqlalchemy import String
from sqlalchemy.orm import Mapped, relationship, mapped_column

from module_21_orm_2.homework.models.base import Base
from module_21_orm_2.homework.models.book import Book


class Author(Base):
    __tablename__ = 'authors'

    # first_name: Mapped[str_50]
    # last_name: Mapped[str_50]

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(35), nullable=False)
    last_name: Mapped[str] = mapped_column(String(35), nullable=False)

    def __repr__(self):
        return f'{self.first_name} {self.last_name}'
    def __getitem__(self, item):
        return getattr(self,item)
    def to_json(self):
        return {c.name: getattr(self,c.name) for c in self.__table__.columns}

    books = relationship('Book', backref='author', lazy='joined',
                              cascade='all, delete-orphan')
