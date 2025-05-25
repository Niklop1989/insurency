from sqlalchemy import select
from datetime import datetime

from sqlalchemy.orm import create_session

from module_21_orm_2.tren.models.base import Base
from module_21_orm_2.tren.models.create_engine import engine,session_create
from module_21_orm_2.tren.models.student import Student
from module_21_orm_2.tren.models.author import Author
from module_21_orm_2.tren.models.book import Book
from module_21_orm_2.tren.models.receiving_book import ReceivingBook


# def create_table():
#     Base.metadata.create_all(engine)
#
# def insert_data():
#     authors = [Author(first_name='Александр',last_name='Пушкин'),
#                Author(first_name='Лев',last_name='Толстой'),
#                Author(first_name='Михаил',last_name='Будгаков')]
#
#     authors[0].books.extend([Book(title='Капитанская дочка',
#                                   count=5,
#                                   release_date=datetime.date(1836, 1, 1)),
#                                     Book(name='Капитанская дочка2',
#                                     count=6,
#                                      release_date=datetime.date(1836, 1, 1))
#                              ])
#     authors[0].books.extend([Book(title='Война и мир',
#                                   count=10,
#                                   release_date=datetime.date(1867, 1, 1)),
#                              Book(title='Анна каренина',
#                                   count=7,
#                                   release_date=datetime.date(1836, 1, 1))
#                              ])
#     authors[0].books.extend([Book(title='Морфий',
#                                   count=5,
#                                   release_date=datetime.date(1925, 1, 1)),
#                              Book(name='Собачье сердце',
#                                   count=3,
#                                   release_date=datetime.date(1926, 1, 1))
#                              ])
#     students = [Student(first_name='Nik',last_name='1',phone='2',
#                         email='3',average_score=4.5,scholaraship=True),
#                 Student(first_name='Vlad', last_name='1', phone='2',
#                         email='3', average_score=4, scholaraship=True)
#                 ]
#
#     session_create.add_all(authors)
#     session_create.add_all(students)
#     session_create.commit()
#
# create_table()
# def drop_create_table():
#     # Base.metadata.drop_all(engine)
#     Base.metadata.create_all(engine)
#
def insert_authors_and_books():
    author_1 = Author(first_name='Лев',last_name='Толстой')
    book_1 = Book(
        title='Война и мир',
        release_date=datetime.strptime('1867-12-01','%Y-%m-%d'))

    book_2 = Book(
        title='Анна Каренина',
        release_date=datetime.strptime('1877-11-13', '%Y-%m-%d'))
    book_3 = Book(
        title='Книга',
        release_date=datetime.strptime('1872-12-01', '%Y-%m-%d'))
    author_1.books.append(book_1)
    author_1.books.append(book_2)
    author_1.books.append(book_3)

    author_2 = Author(first_name='Александр', last_name='Пушкин')
    book_4 = Book(
        title='Евгений Онегин',
        release_date=datetime.strptime('1822-12-01', '%Y-%m-%d'))

    book_5 = Book(
        title='Метель',
        release_date=datetime.strptime('1831-11-13', '%Y-%m-%d'))
    book_6 = Book(
        title='Буря',
        release_date=datetime.strptime('1836-12-01', '%Y-%m-%d'))
    author_2.books.append(book_4)
    author_2.books.append(book_5)
    author_2.books.append(book_6)

    session_create.add_all(author_1,author_2)
    session_create.commit()# def insert_authors_and_books():
#     author_1 = Author(first_name='Лев',last_name='Толстой')
#     book_1 = Book(
#         title='Война и мир',
#         release_date=datetime.strptime('1867-12-01','%Y-%m-%d'))
#
#     book_2 = Book(
#         title='Анна Каренина',
#         release_date=datetime.strptime('1877-11-13', '%Y-%m-%d'))
#     book_3 = Book(
#         title='Книга',
#         release_date=datetime.strptime('1872-12-01', '%Y-%m-%d'))
#     author_1.books.append(book_1)
#     author_1.books.append(book_2)
#     author_1.books.append(book_3)
#
#     author_2 = Author(first_name='Александр', last_name='Пушкин')
#     book_4 = Book(
#         title='Евгений Онегин',
#         release_date=datetime.strptime('1822-12-01', '%Y-%m-%d'))
#
#     book_5 = Book(
#         title='Метель',
#         release_date=datetime.strptime('1831-11-13', '%Y-%m-%d'))
#     book_6 = Book(
#         title='Буря',
#         release_date=datetime.strptime('1836-12-01', '%Y-%m-%d'))
#     author_2.books.append(book_4)
#     author_2.books.append(book_5)
#     author_2.books.append(book_6)
#
#     session_create.add_all(author_1,author_2)
#     session_create.commit()

insert_authors_and_books()
    # @staticmethod
    # def insert_receiving_book():
    #     with create_session() as session:
    #         rb_1 = ReceivingBook(student_id=1,book_id=1,date_of_issue='2025-05-05',date_of_return='2025-06-05')
    #         rb_2 = ReceivingBook(student_id=2, book_id=2, date_of_issue='2025-05-11', date_of_return='2025-06-15')
    #         rb_3 = ReceivingBook(student_id=3, book_id=3, date_of_issue='2025-0-13', date_of_return='2025-06-17')
    #         rb_4 = ReceivingBook(student_id=4, book_id=4, date_of_issue='2025-05-10', date_of_return='2025-06-18')
    #
    #         session.add_all(rb_1,rb_3,rb_4,rb_2)
    #         session.commit()
#     @staticmethod
#     def select_database():
#         with session_create() as session:
#             res_author = session.execute(select(Author)).unique()
#             authors = res_author.all()
#
#             res_book = session.execute(select(Book))
#             books = res_book.all()
#
#             res_student = session.execute(select(Student)).unique()
#             students = res_student.all()
#             print('Authors')
#             for a in authors:
#                 print(f'{a[0].id} {a[0].first_name} {a[0].last_name}')
#
#             print('Books')
#             for b in books:
#                 print(f'{b[0].id} {b[0].title} {a[0].count}')
#
#             print('Students')
#             for s in students:
#                 print(f'{s[0].id} {s[0].first_name} {s[0].last_name}')
#
# @staticmethod
# def insert_students():
#     with session_create() as session:
#         student_1 = Student(first_name='Nikita',last_name='Ivanov',phones='8903123456',email='nik@mail.ru',average_score=2)
#         student_2 = Student(first_name='Vlad', last_name='Petrov', phones='8987654333', email='vlad@mail.ru',
#                             average_score=1)
#         student_3 = Student(first_name='Petr', last_name='Sidorov', phones='8903234556', email='pet@mail.ru',
#                             average_score=3)
#         student_4 = Student(first_name='Jon', last_name='Rembo', phones='832454333', email='jond@mail.ru',
#                             average_score=1)
#         session.add_all(student_1,student_2,student_3,student_4)
#         session.commit()
#


# drop_create_table()
# insert_students()
# create.insert_receiving_book()
# insert_authors_and_books()


























