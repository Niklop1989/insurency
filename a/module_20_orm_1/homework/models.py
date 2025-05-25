import datetime
from typing import Optional

from sqlalchemy import (DateTime, String, Integer, Float, ForeignKey, MetaData,
                        create_engine, Boolean, case, func, Date)
from sqlalchemy.orm import (DeclarativeBase, Session, Mapped, mapped_column,
                            relationship, sessionmaker)
from sqlalchemy.ext.hybrid import hybrid_property
from flask import jsonify, Flask

engine = create_engine("sqlite:///library.db")
session = Session(engine)


# Session = sessionmaker(bind=engine)
# session = Session()

class Base(DeclarativeBase):
    pass


class Book(Base):
    __tablename__ = 'books'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    count: Mapped[int] = mapped_column(Integer, default=0)
    release_date: Mapped[str] = mapped_column(Date)
    author_id: Mapped[int] = mapped_column()

    # id = Column(Integer,primary_key=True)
    # name = Column(String(50),nullable=False)
    # count = Column(Integer,nullable=False)
    # release_date = Column(Date,nullable=False)
    # author_id = Column(Integer,nullable=False)

    def __repr__(self):
        return (f"название {self.name}, кол-во {self.count},\""
                f"дата выпуска {self.release_date}")

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Author(Base):
    __tablename__ = 'authors'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(35), nullable=False)
    surname: Mapped[str] = mapped_column(String(35), nullable=False)

    def __repr__(self):
        return f"имя и фамилия  автора {self.name} {self.surname}"

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Student(Base):
    __tablename__ = 'students'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    surname: Mapped[str] = mapped_column(String(30), nullable=False)
    phone: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    average_score: Mapped[float] = mapped_column(nullable=False)
    scholaraship: Mapped[Boolean] = mapped_column(Boolean, nullable=False)

    @classmethod
    def get_studdents_with_scholarship(cls):
        students = session.query(Student).filter(Student.scholaraship == 1).all()
        stud_list = []
        for s in students:
            stud_list.append(s.to_json())
        # session.close()
        # return jsonify(stud_list)
        return stud_list

    @classmethod
    def get_students_with_top_score(cls, score):
        students = session.query(Student).filter(Student.average_score > score).all()
        stud_list = []
        for s in students:
            stud_list.append(s.to_json())
        return stud_list

    def __repr__(self):
        return (f"имя студента {self.name}, фамилия  {self.surname}\""
                f"score {self.average_score} {self.scholaraship}")

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class ReceivingBook(Base):
    __tablename__ = 'receiving_books'

    id: Mapped[int] = mapped_column(primary_key=True)
    book_id: Mapped[int] = mapped_column(Integer, nullable=False)
    student_id: Mapped[int] = mapped_column(Integer, nullable=False)
    date_of_issue: Mapped[str] = mapped_column(DateTime, nullable=False, default=datetime.datetime.now())
    data_of_return: Mapped[str] = mapped_column(DateTime, nullable=True)

    @hybrid_property
    def count_day_with_book(self):
        end_day = self.data_of_return or datetime.datetime.now()
        return (end_day - self.date_of_issue).days

    @count_day_with_book.expression
    def count_data_with_book(cls):
        end_data = case((cls.date_of_return != None,
                         cls.date_of_return),
                        else_=func.now()
                        )
        return func.juliandday(end_data) - func.julianday(cls.date_of_issue)

    def __repr__(self):
        return (f'{self.book_id},{self.student_id},{self.date_of_issue},{self.data_of_return}')

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
