from datetime import datetime

from flask.sessions import session_json_serializer
# from module_21_orm_2.practice.models import (Book, Student, Author,
#                                              ReceivingBook, session, Base, engine)
from sqlalchemy import update
from flask import Flask, jsonify, abort, request

from module_21_orm_2.homework.models.base import Base
from module_21_orm_2.homework.models.create_engine import engine,session_create
app = Flask(__name__)


@app.before_request
def before_request_func():
    Base.metadata.create_all(engine)


@app.route('/')
def hello_user():
    return "Hello user"

#
# @app.route('/library', methods=['GET'])
# def get_all_books():
#     books_list = []
#     books = session_create.query(Book).all()
#     for b in books:
#         books_list.append(b.to_json())
#     session_create.close()
#     return jsonify(books_list), 200
#
#
# @app.route('/library/<int:book_id>', methods=['GET'])
# def get_book_by_id(book_id):
#     book = session_create.query(Book).filter(Book.id == book_id).one_or_none()
#     if book is None:
#         abort(404)
#     return jsonify(book.to_json()), 200
#
#
# @app.route('/library', methods=['POST'])
# def add_product():
#     name = request.form.get('name', type=str)
#     count = request.form.get('count', type=int)
#     release_date = datetime.strptime(request.form.get('release_date'), "%Y-%m-%d")
#     author_id = request.form.get('author_id', type=int)
#
#     new_book = Book(name=name, count=count, release_date=release_date, author_id=author_id)
#     session_create.add(new_book)
#     session_create.commit()
#     session_create.close()
#     return 'add new book', 201
#
#
# @app.route('/authors', methods=['GET'])
# def get_all_authors():
#     authors_list = []
#     authors = session_create.query(Author).all()
#     for a in authors:
#         authors_list.append(a.to_json())
#     session_create.close()
#     return jsonify(authors_list), 200
#
#
# @app.route('/authors', methods=['POST'])
# def add_new_author():
#     name = request.form.get('name', type=str)
#     surname = request.form.get('surname', type=str)
#
#     new_author = Author(name=name, surname=surname)
#     session_create.add(new_author)
#     session_create.commit()
#     session_create.close()
#     return 'add new author', 201
#
#
# @app.route('/students', methods=['GET'])
# def get_all_students():
#     students_scholarship = Student.get_studdents_with_scholarship()
#     print(f" students get scholarship {students_scholarship}")
#
#     students_avg_hight = Student.get_students_with_top_score(1)
#     print(f'students with top avg {students_avg_hight}')
#
#     students = session.query(Student).all()
#     students_list = []
#     for s in students:
#         students_list.append(s.to_json())
#     session.close()
#     return jsonify(students_list), 200
#
#
# @app.route('/students', methods=['POST'])
# def add_students():
#     name = request.form.get('name', type=str)
#     surname = request.form.get('surname', type=str)
#     phone = request.form.get('phone', type=str)
#     email = request.form.get('email', type=str)
#     average_score = request.form.get('average_score', type=float)
#     scholaraship = request.form.get('scholarship')
#     if scholaraship == 'yes':
#         scholaraship = True
#     else:
#         scholaraship = False
#     new_student = Student(name=name, surname=surname, phone=phone,
#                           email=email, average_score=average_score,
#                           scholaraship=scholaraship)
#     session.add(new_student)
#     session.commit()
#     session.close()
#     return 'add new student', 201
#
#
# @app.route('/take_book', methods=['POST'])
# def take_book():
#     book_id = request.form.get('book_id', type=int)
#     student_id = request.form.get('student_id', type=int)
#     data_of_return = datetime.strptime(request.form.get('data_of_return'), '%Y-%m-%d')
#
#     new_take_book = ReceivingBook(book_id=book_id, student_id=student_id,
#                                   data_of_return=data_of_return)
#     session.add(new_take_book)
#
#     # записываем в книги какую книгу взяли
#     book = session.query(Book).filter(Book.id == book_id).one_or_none()
#     # убавляем счетчик кол-ва взятой книги
#     session.execute(update(Book).filter(Book.id == book_id).values(count=book.count - 1))
#     session.commit()
#     session.close()
#     return 'you take book', 201
#
#
# @app.route('/return_book', methods=['POST'])
# def return_book():
#     #  return book in library
#     book_id = request.form.get('book_id', type=int)
#     student_id = request.form.get('student_id', type=int)
#
#     my_book = session.query(ReceivingBook).filter(ReceivingBook.book_id == book_id
#                                                   and ReceivingBook.student_id == student_id).one_or_none()
#     if my_book:
#         book = session.query(Book).filter(Book.id == book_id).one_or_none()
#
#         # count book +1
#         session.execute(update(Book).filter(Book.id == book_id).values(count=book.count + 1))
#         # delete book from ReceivingBook
#         session.query(ReceivingBook).filter(ReceivingBook.book_id == my_book.id).delete()
#         session.commit()
#         session.close()
#         return 'yoy return book'
#     return 'don t hve this book'
#
#
# @app.route('/receiving_book', methods=['GET'])
# def receiving_books():
#     receiving_books = session.query(ReceivingBook).all()
#     books_list = []
#     for r in receiving_books:
#         books_list.append(r.to_json())
#     session.close()
#     return jsonify(books_list), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0')
