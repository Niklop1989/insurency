from sqlalchemy import select
from sqlalchemy.orm import Session
from main import User,engine,Address

session = Session(engine)

res = (select(Address).join(Address.user)
       .where(Address.email_address=='nikitaivan@mail.ru'))

address = session.scalars(res).one()
print(address)


# Очень часто приходится делать запросы сразу к нескольким таблицам,
# и в SQL ключевое слово JOIN является основным способом, с помощью которого это
# происходит. Конструкция Select создает соединения, используя метод Select.join():