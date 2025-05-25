from sqlalchemy.orm import Session
from main import User,Address,engine

with Session(engine) as session:
    nikita = User(
        name='Nikita',
        fullname='Lopantcsev',
        addresses=[Address(email_address="nikitaivan@mail.ru")]
    )

session.add_all([nikita])
session.commit()


# Теперь мы готовы к вставке данных в базу данных. Для этого мы создаем экземпляры классов User и Address,
# у которых уже есть метод __init__(), автоматически созданный в процессе декларативного отображения.
# Затем мы передаем их в базу данных с помощью объекта Session, который использует метод Engine для взаимодействия с базой данных.
# Метод Session.add_all() используется здесь для добавления нескольких объектов одновременно, а метод Session.commit()
# будет использоваться для flush любых ожидающих изменений в базе данных и затем commit текущей транзакции базы данных,
# которая всегда находится в процессе, когда используется Session: