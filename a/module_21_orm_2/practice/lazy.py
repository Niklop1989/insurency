import datetime
from typing import Optional

from sqlalchemy import (DateTime, String, Integer, Float, ForeignKey, MetaData,
                        create_engine, Boolean, case, func, Date, Table, Column)
from sqlalchemy.orm import (DeclarativeBase, Session, Mapped, mapped_column,
                            relationship, sessionmaker,joinedload)
from sqlalchemy.ext.hybrid import hybrid_property

engine =  create_engine("sqlite:///lazy.db",echo=True)
# echo = True для того что бы в консоль писались все запросы
session = Session(engine)

class Base(DeclarativeBase):
    pass


class Parents(Base):
    __tablename__ = 'parent'

    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    children = relationship('Child',lazy='select')
    # lazy="joined,subquery,selectin,raise,noload"

class Child(Base):
    __tablename__ = 'child'

    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    parent_id:Mapped[int] = mapped_column(ForeignKey('parent.id'))


if __name__=='__main__':
    Base.metadata.create_all(engine)

    parents = Parents()

    session.add(parents)
    child_one = Child(parent_id=1)
    child_two = Child(parent_id=1)

    session.add(child_one)
    session.add(child_two)
    session.commit()

    my_parent = session.query(Parents).first()
    my_child = my_parent.children
    for c in my_child:
        print(c)

    print('custom lazy')
    q = session.query(Parents).options(joinedload(Parents.children)).all()
    print(q)
