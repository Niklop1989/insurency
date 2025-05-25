import datetime
from typing import Optional, List

from sqlalchemy import (DateTime, String, Integer, Float, ForeignKey, MetaData,
                        create_engine, Boolean, case, func, Date, Column)
from sqlalchemy.orm import (DeclarativeBase, Session, Mapped, mapped_column,
                            relationship, sessionmaker, joinedload, backref)
from sqlalchemy.ext.hybrid import hybrid_property
from flask import jsonify, Flask


engine = create_engine("sqlite:///library_lesson21.db")
session = Session(engine)


# Session = sessionmaker(bind=engine)
# session = Session()

class Base(DeclarativeBase):
    pass


class Book(Base):
    __tablename__ = 'books'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    count: Mapped[int] = mapped_column(Integer, default=1)
    release_date: Mapped[str] = mapped_column(Date,nullable=False)
    author_id: Mapped[int] = mapped_column(Integer,
                                           ForeignKey('authors.id'),nullable=False)
    author = relationship('Author',backref=backref('books',
                                      cascade='all, '
                                              'delete-orphan',
                                      lazy='select'))
    students = relationship('ReceivingBook',back_populates='book')

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
    scholaraship:Mapped[Boolean] = mapped_column(Boolean, nullable=False)

    books = relationship('ReceivingBook',back_populates='student')

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
    book_id: Mapped[int] = mapped_column(Integer, ForeignKey('books.id'),nullable=False)
    student_id: Mapped[int] = mapped_column(Integer, ForeignKey('students.id'),nullable=False)
    date_of_issue: Mapped[str] = mapped_column(DateTime, nullable=False, default=datetime.datetime.now())
    data_of_return: Mapped[str] = mapped_column(DateTime, nullable=True)

    student = relationship('Student',back_populates='books')
    book = relationship('Book',back_populates='students')


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


def insert_data():
    authors = [Author(name='Александр',surname='Пушкин'),
               Author(name='Лев',surname='Толстой'),
               Author(name='Михаил',surname='Будгаков')]

    authors[0].books.extend([Book(name='Капитанская дочка',
                                  count=5,
                                  release_date=datetime.date(1836, 1, 1)),
                                    Book(name='Капитанская дочка2',
                                    count=6,
                                     release_date=datetime.date(1836, 1, 1))
                             ])
    authors[0].books.extend([Book(name='Война и мир',
                                  count=10,
                                  release_date=datetime.date(1867, 1, 1)),
                             Book(name='Анна каренина',
                                  count=7,
                                  release_date=datetime.date(1836, 1, 1))
                             ])
    authors[0].books.extend([Book(name='Морфий',
                                  count=5,
                                  release_date=datetime.date(1925, 1, 1)),
                             Book(name='Собачье сердце',
                                  count=3,
                                  release_date=datetime.date(1926, 1, 1))
                             ])
    students = [Student(name='Nik',surname='1',phone='2',
                        email='3',average_score=4.5,scholaraship=True),
                Student(name='Vlad', surname='1', phone='2',
                        email='3', average_score=4, scholaraship=True)
                ]

    session.add_all(authors)
    session.add_all(students)
    session.commit()

def give_me_a_book():
    nikita = session.query(Student).filter(Student.name=='Nik').one()
    vlad = session.query(Student).filter(Student.name=='Vlad').one()
    books_to_nik = session.query(Book).filter(Author.surname=='Толстой',
                                              Author.id==Book.author_id).all()
    books_to_vlad = session.query(Book).filter(Book.id.in_([1,2,3])).all()

    for book in books_to_nik:
        receiving_book = ReceivingBook()
        receiving_book.book = book
        receiving_book.student = nikita
        session.add(receiving_book)

    for book in books_to_vlad:
        receiving_book = ReceivingBook()
        receiving_book.book = book
        receiving_book.student = vlad
        session.add(receiving_book)
    session.commit()


if __name__=='__main__':
    Base.metadata.create_all(bind=engine)
    # insert_data()
    check_exist = session.query(Author).all()
    if not check_exist:
        insert_data()
        give_me_a_book()

    # author_q = session.query(Author.id).filter_by(name='Лев').subquery()
    # print('+++',author_q)
    # books_by_lev = session.query(Book).filter(Book.author_id.in_(author_q)).all()
    # print('-----',books_by_lev)
    #
    students = session.query(Student.name.label('student_name')).all()
    for s in students:
        if s.student_name == 'Nik':
            print('Nik')
    # count all books in library
    # по убыванию
    count_of_books = session.query(func.sum(Book.count)).scalar()

    # count book by author
    count_books_by_author = session.query(func.sum(Book.count),
                                          Author.name,Author.surname) \
                                    .filter(Book.author_id == Author.id) \
                                    .group_by(Author.id).order_by(func.sum(Book.count).desc()).all()
    # получаем книги сщ связанными авторами - жадная загрузка
    books_with_authors = session.query(Book).options(joinedload(Book.author)).all()

    # join  для двух таблиц
    book_join_author = session.query(Book).join(Book.author).all()

    # join subquery

    author_q = session.query(Author).filter_by(name='Михаил').subquery()
    michail_books = session.query(Book).join(author_q,Book.author_id==author_q.c.id).all()

    print('end')


