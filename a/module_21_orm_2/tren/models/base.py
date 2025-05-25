from typing import Annotated
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy.orm import DeclarativeBase

str_150 = Annotated[str, 150]
str_50 = Annotated[str, 50]
int_ = Annotated[int,mapped_column(autoincrement=True,primary_key=True)]

class Base(DeclarativeBase):
    pass