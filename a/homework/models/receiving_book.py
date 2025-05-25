import datetime
from sqlalchemy import ForeignKey, case, func, Integer, DateTime
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped,mapped_column,relationship
from module_21_orm_2.tren.models.base import Base
from module_21_orm_2.tren.models.author import Author
from module_21_orm_2.tren.models.student import Student


class ReceivingBook(Base):
    __tablename__ = 'receiving_books'

    id: Mapped[int] = mapped_column(primary_key=True)
    book_id: Mapped[int] = mapped_column(Integer, ForeignKey('books.id'), nullable=False)
    student_id: Mapped[int] = mapped_column(Integer, ForeignKey('students.id'), nullable=False)
    date_of_issue: Mapped[str] = mapped_column(DateTime, nullable=False, default=datetime.datetime.now())
    data_of_return: Mapped[str] = mapped_column(DateTime, nullable=True)

    student = relationship('Student', back_populates='books')
    book = relationship('Book', back_populates='students')

    students_with_book: Mapped['Student'] = relationship(
        back_populates='student_receiving_books',
        cascade='all, delete',
        lazy='joined'
    )

    @hybrid_property
    def count_day_with_book(self):
        end_date = self.date_of_return or datetime.datetime.now()
        return (end_date - self.date_of_isue).days


    @count_day_with_book.expression
    def count_data_with_book(cls):
        end_data = case((cls.date_of_return != None,
                         cls.date_of_return),
                        else_=func.now()
                        )
        return func.juliandday(end_data) - func.julianday(cls.date_of_issue)


    def __repr__(self):
        return f'{self.book_id} - {self.student_id} - {self.date_of_isue}'

    def __getitem__(self, item):
        return getattr(self,item)

    def to_json(self):
        return {c.first_name: f'{getattr(self, c.first_name)}'
                for c in self.__table__.columns}



