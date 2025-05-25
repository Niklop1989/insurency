import datetime
from typing import Optional

from sqlalchemy import (DateTime, String, Integer, Float, ForeignKey, MetaData,
                        create_engine, Boolean, case, func, Date, Table, Column)
from sqlalchemy.orm import (DeclarativeBase, Session, Mapped, mapped_column,
                            relationship, sessionmaker)
from sqlalchemy.ext.hybrid import hybrid_property

engine =  create_engine("sqlite:///iner.db")
session = Session(engine)

class Base(DeclarativeBase):
    pass


# internation_table = Table('international',Base.metadata,
#                           Column('parent_id',ForeignKey('parent.id'),
#                                  primary_key=True),
#                           Column('child_id',ForeignKey('child.id'),
#                                  primary_key=True))

class International(Base):
    __tablename__ = 'international'

    id:Mapped[int] = mapped_column(primary_key=True)
    parent_id:Mapped[int] = mapped_column(ForeignKey('parent.id'))
    child_id:Mapped[int] = mapped_column(ForeignKey('child.id'))

class Parents(Base):
    __tablename__ = 'parent'

    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    children = relationship('Child',secondary='international',
                         back_populates='parent')
    # secondary для связи таблицы

class Child(Base):
    __tablename__ = 'child'

    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    parent = relationship('Parents',secondary='international',
                          back_populates='children')


if __name__=='__main__':
    Base.metadata.create_all(engine)

    father = Parents()
    mother = Parents()

    son = Child()
    doughter = Child()

    father.children.extend([son,doughter])

    son.parent.append(mother)
    doughter.parent.append(mother)

    session.add(father)
    session.add(mother)
    session.add(doughter)
    session.add(son)
    session.commit()

    father.children.remove(doughter)