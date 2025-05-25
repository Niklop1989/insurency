import datetime
from typing import List, Any

from sqlalchemy import ForeignKey, Integer, Date, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from module_21_orm_2.homework.models.create_session import Base


class Book(Base):
    __tablename__ = 'books'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    count: Mapped[int] = mapped_column(Integer, default=1)
    release_date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey('authors.id'),
                                           nullable=False)
    author: Mapped[List[Any]] = relationship('Author', backref='books',
                                             lazy='select',
                                             cascade='all, delete-orphan',
                                             single_parent=True)
    students: Mapped[List[Any]] = relationship('ReceivingBook',
                                               back_populates='book')

    def __repr__(self):
        return f'Book(id={self.id}, title={self.title})'

    def __getitem__(self, item):
        return getattr(self, item)

    def to_json(self):
        to_json = {c.name: f'{getattr(self, c.name)}' for c in self.__table__.columns}
        return to_json
