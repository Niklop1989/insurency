import datetime
from typing import Optional

from sqlalchemy import (DateTime, String, Integer, Float, ForeignKey, MetaData,
                        create_engine, Boolean, case, func, Date, Table, Column)
from sqlalchemy.orm import (declarative_base,DeclarativeBase, Session, Mapped, mapped_column,
                            relationship, sessionmaker)
from sqlalchemy.ext.hybrid import hybrid_property

engine =  create_engine("sqlite:///mass.db")
session = Session(engine)

class Base(DeclarativeBase):
    pass

class Parent(Base):
    __tablename__ = 'parents'

    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    name:Mapped[str] = mapped_column(String(50),nullable=False)

if __name__=='__main__':
    Base.metadata.create_all(engine)

    parent_1 = Parent(name='Nikita')
    pareny_2 = Parent(name='Vlad')
    parent_3 = Parent(name='Lera')

    session.bulk_save_objects([parent_1,pareny_2,parent_3])
    session.commit()

    inser_parents = [{"name":"Nikita2",
                     "name":"Vlad2",
                     "name":"Lera2"}]
    session.bulk_insert_mappings(Parent, inser_parents)
    session.commit()

    update_parents = [
        {'id':1,'name':'Nikita3',
         'id':2,'name':'Vlad3',
         'id':3,'name':'Vlad4'}
    ]
    session.bulk_update_mappings(Parent,update_parents)
    session.commit()
