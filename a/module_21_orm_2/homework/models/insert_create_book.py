from sqlalchemy import select
import datetime

from module_21_orm_2.homework.models.book import Book
from module_21_orm_2.homework.models.author import Author
from module_21_orm_2.homework.models.student import Student
from module_21_orm_2.homework.models.create_session import sessions, engine
from module_21_orm_2.homework.models.create_session import Base


def create_table():
    Base.metadata.create_all(engine)


def insert_data():
    authors = [Author(first_name='Александр', last_name='Пушкин'),
               Author(first_name='Лев', last_name='Толстой'),
               Author(first_name='Михаил', last_name='Будгаков')]

    authors[0].books.extend([Book(title='Капитанская дочка',
                                  count=5,
                                  release_date=datetime.date(1836, 1, 1)),
                             Book(title='Капитанская дочка2',
                                  count=6,
                                  release_date=datetime.date(1836, 1, 1))
                             ])
    authors[0].books.extend([Book(title='Война и мир',
                                  count=10,
                                  release_date=datetime.date(1867, 1, 1)),
                             Book(title='Анна каренина',
                                  count=7,
                                  release_date=datetime.date(1836, 1, 1))
                             ])
    authors[0].books.extend([Book(title='Морфий',
                                  count=5,
                                  release_date=datetime.date(1925, 1, 1)),
                             Book(title='Собачье сердце',
                                  count=3,
                                  release_date=datetime.date(1926, 1, 1))
                             ])
    students = [Student(first_name='Nik', last_name='1', phone='2',
                        email='3', average_score=4.5, scholarship=True),
                Student(first_name='Vlad', last_name='1', phone='2',
                        email='3', average_score=4, scholarship=True)
                ]

    sessions.add_all(authors)
    sessions.add_all(students)
    sessions.commit()


def insert_students():
    student_1 = [Student(first_name='Nikita', last_name='Ivanov', phone='8903123456', email='nik@mail.ru',
                         average_score=2.3, scholarship=True),
                 Student(first_name='Vlad', last_name='Petrov', phone='8987654333', email='vlad@mail.ru',
                         average_score=2.2, scholarship=True),
                 Student(first_name='Petr', last_name='Sidorov', phone='8903234556', email='pet@mail.ru',
                         average_score=3.3, scholarship=True),
                 Student(first_name='Jon', last_name='Rembo', phone='832454333', email='jond@mail.ru',
                         average_score=1.1, scholarship=True)]
    sessions.add_all(student_1),
    sessions.commit()


def select_database():
    res_author = sessions.execute(select(Author)).unique()
    authors = res_author.all()

    res_book = sessions.execute(select(Book))
    books = res_book.all()

    res_student = sessions.execute(select(Student)).unique()
    students = res_student.all()
    print('Authors')
    for a in authors:
        print(f'{a[0].id} {a[0].first_name} {a[0].last_name}')

    print('Books')
    for b in books:
        print(f'{b[0].id} {b[0].title} {b[0].count}')

    print('Students')
    for s in students:
        print(f'{s[0].id} {s[0].first_name} {s[0].last_name}')

insert_students()