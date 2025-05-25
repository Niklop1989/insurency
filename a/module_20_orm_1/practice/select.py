from sqlalchemy import select
from sqlalchemy.orm import Session
from main import User,engine

session = Session(engine)

res = select(User).where(User.name.in_(['Nikita']))

for user in session.scalars(res):
    print(user)


#
# Имея несколько строк в базе данных, вот простейшая форма создания оператора SELECT для загрузки некоторых объектов.
# Для создания операторов SELECT мы используем функцию select() для создания нового объекта Select, который затем вызываем с помощью Session.
# Метод, который часто бывает полезен при запросе объектов ORM, -
# это метод Session.scalars(), который возвращает объект ScalarResult, перебирающий выбранные нами объекты ORM: