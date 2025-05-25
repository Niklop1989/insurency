import datetime
from typing import Optional

from sqlalchemy import (DateTime, String, Integer, Float, ForeignKey, MetaData,
                        create_engine, Boolean, case, func, Date)
from sqlalchemy.orm import (DeclarativeBase, Session, Mapped, mapped_column,
                            relationship, sessionmaker)
from sqlalchemy.ext.hybrid import hybrid_property

engine =  create_engine("sqlite:///many_to_on.db")
session = Session(engine)

class Base(DeclarativeBase):
    pass

class Parents(Base):
    __tablename__ = 'parents'

    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    children_id:Mapped[int] = mapped_column(ForeignKey('children.id'))
    child = relationship('Child',backref='parents')

class Child(Base):
    __tablename__ = 'children'

    id:Mapped[int] = mapped_column(primary_key=True)

if __name__=='__main__':
    Base.metadata.create_all(engine)

    child=Child()
    session.add(child)
    session.commit()

    parent_one = Parents(children_id=1)
    parent_two = Parents(children_id=1)
    session.add(parent_one)
    session.add(parent_two)
    session.commit()

    my_children = session.query(Parents).filter(Parents.children_id==1).all()
    my_parents = session.query(Child).all()
    print(my_parents,my_children)


