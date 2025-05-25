from sqlalchemy import select
from sqlalchemy.orm import Session
from main import User,engine,Address

session = Session(engine)

res = select(User).where(User.name == 'Nikita')
nikita = session.scalars(res).one()

# nikita.addresses.append(Address(email_address='nik@mail.ru'))

nikita.email_address = 'Nik@,'
session.commit()

# Объект Session в сочетании с нашими ORM-сопоставленными классами User и
# Address автоматически отслеживает изменения в объектах по мере их внесения,
# что приводит к SQL-запросам, которые будут выданы при следующей очистке Session.
# Ниже мы изменим один адрес электронной почты, связанный с «sandy»,
# а также добавим новый адрес электронной почты к «patrick», после того как выполним
# SELECT для получения строки для «patrick»: