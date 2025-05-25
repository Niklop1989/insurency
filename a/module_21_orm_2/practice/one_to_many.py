import datetime
from typing import Optional

from sqlalchemy import (DateTime, String, Integer, Float, ForeignKey, MetaData,
                        create_engine, Boolean, case, func, Date)
from sqlalchemy.orm import (DeclarativeBase, Session, Mapped, mapped_column,
                            relationship, sessionmaker)
from sqlalchemy.ext.hybrid import hybrid_property

engine =  create_engine("sqlite:///one_to_many.db")
session = Session(engine)

class Base(DeclarativeBase):
    pass
class Parents(Base):
    __tablename__ = 'parents'

    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    children = relationship('Child',back_populates='parent')
    # children = relationship('Child',backref='parent')

class Child(Base):
    __tablename__ = 'child'

    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    parent_id:Mapped[int] = mapped_column(Integer,ForeignKey('parents.id'))
    parent = relationship('Parents',back_populates='children')


if __name__=='__main__':
    Base.metadata.create_all(engine)

    parent = Parents()
    session.add(parent)
    session.commit()

    chaild_one = Child(parent_id=1)
    chaild_two = Child(parent_id=1)
    session.add(chaild_one)
    session.add(chaild_two)
    session.commit()

    my_children = session.query(Child).filter(Child.parent_id==1).all()
    my_parents = session.query(Parents).all()
    print(my_parents,my_children)


