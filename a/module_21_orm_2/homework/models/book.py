import datetime
from sqlalchemy import ForeignKey, Integer, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship, backref

from module_21_orm_2.homework.models.base import Base

class Book(Base):
    __tablename__ = 'books'

    # title: Mapped[str_150]
    # count: Mapped[int] = mapped_column(default=1)
    # release_date: Mapped[datetime.date]
    # author_id: Mapped[int] = mapped_column(ForeignKey('authors.id', ondelete='CASCADE'))

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    count: Mapped[int] = mapped_column(Integer, default=1)
    release_date: Mapped[str] = mapped_column(Date, nullable=False)
    author_id: Mapped[int] = mapped_column(Integer,
                                           ForeignKey('authors.id'), nullable=False)
    author = relationship('Author', backref=backref('books',
                                                    cascade='all, '
                                                            'delete-orphan',
                                                    lazy='select'))
    students = relationship('ReceivingBook', back_populates='book')

    def __repr__(self):
        return f'Book(id={self.id}, title={self.title})'

    def __getitem__(self, item):
        return getattr(self, item)

    def to_json(self):
        to_json = {c.name: f'{getattr(self, c.name)}' for c in self.__table__.columns}
        return to_json
