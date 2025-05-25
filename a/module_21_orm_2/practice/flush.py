import datetime
from typing import Optional

from sqlalchemy import (DateTime, String, Integer, Float, ForeignKey, MetaData,
                        create_engine, Boolean, case, func, Date, Table, Column)
from sqlalchemy.orm import (declarative_base,DeclarativeBase, Session, Mapped, mapped_column,
                            relationship, sessionmaker)
from sqlalchemy.ext.hybrid import hybrid_property

engine =  create_engine("sqlite:///iner.db")
session = Session(engine)

class Base(DeclarativeBase):
    pass

class Parent(Base):
    __tablename__ = 'parents'

    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    name:Mapped[str] = mapped_column(String(50),nullable=False)

if __name__=='__main__':
    Base.metadata.create_all(engine)

    parent = Parent(name='Nikita')
    session.add(parent)

    q1 = session.query(Parent).all()
    print('q1')
    session.commit()

    new_session = session
    new_session.autoflush=False

    new_session.add(Parent(name='Vlad'))
    q2 = new_session.query(Parent).all()
    print('q2')