import datetime
from typing import Optional

from sqlalchemy import (DateTime, String, Integer, Float, ForeignKey, MetaData,
                        create_engine, Boolean, case, func, Date)
from sqlalchemy.orm import (DeclarativeBase, Session, Mapped, mapped_column,
                            relationship, sessionmaker)
from sqlalchemy.ext.hybrid import hybrid_property

engine =  create_engine("sqlite:///one_to_one.db")
session = Session(engine)

class Base(DeclarativeBase):
    pass

class Parents(Base):
    __tablename__ = 'parent'

    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    child = relationship('Child',back_populates='parent',uselist=False)
    # uselist=False запрет связывать со множеством значений

class Child(Base):
    __tablename__ = 'child'

    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    parent_id:Mapped[int] = mapped_column(Integer,ForeignKey('parent.id'),unique=True)
    parent = relationship('Parents',back_populates='child')
    # unoque только оин родителб

if __name__=='__main__':
    Base.metadata.create_all(engine)

    parent = Parents()
    session.add(parent)
    session.commit()

    child_one = Child(parent_id=1)
    session.add(child_one)
    session.commit()

    # chaild_two = Child(parent_id=1)
    # session.add(chaild_two)
    # session.commit()