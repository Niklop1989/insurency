import calendar
import csv
import os.path
from crypt import methods
from datetime import datetime, date
from itertools import chain

from flask.sessions import session_json_serializer

from table_library.models.author import Author
from table_library.models.student import Student
from table_library.models.receiving_book import ReceivingBook
from table_library.models.book import Book
from table_library.models.create_session import engine, sessions
from table_library.models.create_session import Base

from sqlalchemy import update, select, func, delete
from flask import Flask, jsonify, abort, request

app = Flask(__name__)


@app.before_request
def before_request_func():
    Base.metadata.create_all(engine)


@app.route('/')
def hello_user():
    return "Hello user"


@app.route('/library', methods=['GET'])
def get_all_books():
    books_list = []
    books = sessions.query(Book).all()
    for b in books:
        books_list.append(b.to_json())
    sessions.close()
    return jsonify(books_list), 200


@app.route('/library/<int:book_id>', methods=['GET'])
def get_book_by_id(book_id):
    book = sessions.query(Book).filter(Book.id == book_id).one_or_none()
    if book is None:
        abort(404)
    return jsonify(book.to_json()), 200


@app.route('/library', methods=['POST'])
def add_product():
    name = request.form.get('title', type=str)
    count = request.form.get('count', type=int)
    release_date = datetime.strptime(request.form.get('release_date'), "%Y-%m-%d")
    author_id = request.form.get('author_id', type=int)

    new_book = Book(title=name, count=count, release_date=release_date, author_id=author_id)
    sessions.add(new_book)
    sessions.commit()
    sessions.close()
    return 'add new book', 201


@app.route('/authors', methods=['GET'])
def get_all_authors():
    authors_list = []
    authors = sessions.query(Author).all()
    for a in authors:
        authors_list.append(a.to_json())
    sessions.close()
    return jsonify(authors_list), 200


@app.route('/authors', methods=['POST'])
def add_new_author():
    name = request.form.get('first_name', type=str)
    surname = request.form.get('last_name', type=str)

    new_author = Author(first_name=name, last_name=surname)
    sessions.add(new_author)
    sessions.commit()
    sessions.close()
    return 'add new author', 201

@app.route('/delete_author',methods=['POST'])
def delete_author():
    author_id = request.form.get('author_id',type=int)
    sessions.execute(delete(Author).filter(Author.id==author_id))
    sessions.commit()

    authors = sessions.execute(select(Author)).unique().all()
    authors_list = []
    for a in authors:
        authors_list.append(a[0].to_json())
    return authors_list


@app.route('/students', methods=['GET'])
def get_all_students():
    students_scholarship = Student.get_student_by_scholarship()
    print(f" students get scholarship {students_scholarship}")

    students_avg_hight = Student.get_status_by_high_avarege_ckore(1)
    print(f'students with top avg {students_avg_hight}')

    students = sessions.query(Student).all()
    students_list = []
    for s in students:
        students_list.append(s.to_json())
    sessions.close()
    return jsonify(students_list), 200


@app.route('/students', methods=['POST'])
def add_students():
    first_name = request.form.get('first_name', type=str)
    last_name = request.form.get('last_name', type=str)
    phone = request.form.get('phone', type=str)
    email = request.form.get('email', type=str)
    average_score = request.form.get('average_score', type=float)
    scholarship = request.form.get('scholarship')
    if scholarship == 'yes':
        scholarship = True
    else:
        scholarship = False
    new_student = Student(first_name=first_name, last_name=last_name, phone=phone,
                          email=email, average_score=average_score,
                          scholarship=scholarship)
    sessions.add(new_student)
    sessions.commit()
    sessions.close()
    return 'add new student', 201


@app.route('/take_book', methods=['POST'])
def take_book():
    book_id = request.form.get('book_id', type=int)
    student_id = request.form.get('student_id', type=int)
    data_of_return = datetime.strptime(request.form.get('data_of_return'), '%Y-%m-%d')

    new_take_book = ReceivingBook(book_id=book_id, student_id=student_id,
                                  data_of_return=data_of_return)
    sessions.add(new_take_book)

    # записываем в книги какую книгу взяли
    book = sessions.query(Book).filter(Book.id == book_id).one_or_none()
    # убавляем счетчик кол-ва взятой книги
    sessions.execute(update(Book).filter(Book.id == book_id).values(count=book.count - 1))
    sessions.commit()

    return 'you take book', 201


@app.route('/return_book', methods=['POST'])
def return_book():
    #  return book in library
    book_id = request.form.get('book_id', type=int)
    student_id = request.form.get('student_id', type=int)

    my_book = sessions.execute(select(ReceivingBook.id).filter(ReceivingBook.book_id == book_id,
                                                               ReceivingBook.student_id == student_id)).unique().one_or_none()
    if my_book:
        # how many book we have
        book = sessions.execute(select(Book.count).filter(Book.id == book_id)).scalar()

        # count book +1
        sessions.execute(update(Book).filter(Book.id == book_id).values(count=book + 1))

        # ставим время возврата
        sessions.execute(
            update(ReceivingBook).filter(ReceivingBook.id == my_book[0]).values(data_of_return=datetime.now()))

        sessions.commit()
        sessions.close()

        # имена тех кто взял книги
        res_name = sessions.execute(select(
            Student.id.in_(list(chain(*sessions.execute(select(ReceivingBook.student_id)
                                                        .filter(ReceivingBook.data_of_return == None)).all())))
        ))
        students = res_name.all()
        students_list = []
        for s in students:
            students_list.append({"id": s[0], "first_name": s[1], "last_name": s[2]})
        print(students_list)
        # список книг которые взяли студенты
        res_book = sessions.execute(select(Book.id, Book.title).where(Book.id.in_(list(chain(*sessions.execute(select(
            ReceivingBook.book_id).filter(ReceivingBook.data_of_return == None)).all())))))
        boooks = res_book.all()
        books_list = []
        for b in boooks:
            books_list.append({'id': b[0], 'title': b[1]})
        print(books_list)
        return 'yoy return book'
    return 'don t hve this book'


@app.route('/receiving_book', methods=['GET'])
def receiving_books():
    receiving_books = sessions.query(ReceivingBook).all()
    books_list = []
    for r in receiving_books:
        books_list.append(r.to_json())
    sessions.close()
    return jsonify(books_list), 200


@app.route('/find_book', methods=['POST'])
def find_book():
    res = request.form.get('search', type=str)
    search = "%{}%".format(res)
    books = sessions.execute(select(Book).filter(Book.title.like(search))).unique().all()
    books_list = []
    for b in books:
        books_list.append(b[0].to_json())
    return books_list


@app.route('/books_by_author', methods=['POST'])
def get_book_by_author():
    author_id = request.form.get('author_id', type=int)
    res = sessions.execute(select(Book.count).filter_by(author_id=author_id)).all()
    count = 0
    for c in res:
        count += c[0]
    authors = sessions.execute(select(Author)).unique().all()
    authors_list = []
    for a in authors:
        authors_list.append(a[0].to_json())
    sessions.commit()
    sessions.close()
    print(count)
    return authors_list


@app.route('/book_recommend', methods=['POST'])
def book_recommend():
    student_id = request.form.get('student_id', type=int)
    # id книг которые читал
    books = sessions.query(ReceivingBook.book_id).filter_by(student_id=student_id)

    # id автора котрый написал эти книги
    authors = sessions.query(Book.id).where(Book.id.in_(books))

    # получаем id книг которых нет в books но есть в authors
    recommend_book = sessions.query(Book).where(Book.id.notin_(books)).where(Book.author_id.in_(authors))
    books_list = []
    for b in books:
        books_list.append(b.to_json())
    return books_list

    # студенты которые брали книги
    res = sessions.execute(select(Student).where(Student.id.in_(
        list(chain(*sessions.execute(select(ReceivingBook.student_id)).all()))
    )))
    stdents = res.all()
    students_list = []
    for s in stdents:
        students_list.append(s.to_json())
    return students_list


@app.route('/get_book_month', methods=['POST'])
def get_book_month():
    month = request.form.get('month', type=int)
    days = calendar.monthrange(datetime.now().year, month)[1]

    books = sessions.execute(select(ReceivingBook).filter(
        ReceivingBook.date_of_issue.between(
            date(2025, month, 1), date(2025, month, days)
        ))).unique().all()
    return f'month {month} books {books}'


@app.route('/popular_book', methods=['GET'])
def popular_book():
    # самая популярная книга среди студентов
    books = sessions.query(ReceivingBook.book_id, func.count(ReceivingBook.book_id)).where(
        ReceivingBook.student_id.in_(sessions.query(Student.id).where(Student.average_score > 4))
    ).group_by(ReceivingBook.book_id).all()

    book_id = max(books, key=lambda book: book[1])[0]
    book_title = sessions.execute(select(Book.title).filter_by(id=book_id)).first()
    return f'{book_title}'


@app.route('/top_ten', methods=['GET'])
def top_ten_students():
    students = sessions.query(Student).where(Student.id.in_(sessions.query(ReceivingBook.student_id).filter(
        ReceivingBook.date_of_issue.between(date(2025, 5, 1), date(2025, 6, 2))
    ).group_by(ReceivingBook.student_id).order_by(func.count(ReceivingBook.book_id).desc()).limit(10))).all()
    students_list = []
    for s in students:
        students_list.append(s.to_json())
    return students_list


@app.route('/load_csv_file', methods=['POST'])
def load_csv_file():
    file = request.files['csv_fils']
    file.save(os.path.join(file.filename))
    with open(file.filename, 'r') as filename:
       try:
        fieldname = ['id','first_name','last_name','phone','email','average_score','scholarship']
        # fieldname = ['first_name','last_name','phone','email']
        read_file = csv.DictReader(f=filename, fieldnames=fieldname, delimiter=";")
        dict_list = []

        for string in read_file:
            print(string)
            dict_list.append(string[0])
       except Exception as exc:
           print(exc)
    sessions.bulk_insert_mappings(Student, dict_list)
    sessions.commit()
    return f'данные загружены'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
