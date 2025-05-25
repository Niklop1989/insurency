import datetime
from typing import Optional, List

from sqlalchemy import (DateTime, String, Integer, Float, ForeignKey, MetaData,
                        create_engine, Boolean, case, func, Date, Column)
from sqlalchemy.orm import (DeclarativeBase, Session, Mapped, mapped_column,
                            relationship, sessionmaker, joinedload, backref)
from sqlalchemy.ext.hybrid import hybrid_property
from flask import jsonify, Flask

engine = create_engine("sqlite:///library_lesson21.db")
sessions = Session(engine)

class Base(DeclarativeBase):
    pass
