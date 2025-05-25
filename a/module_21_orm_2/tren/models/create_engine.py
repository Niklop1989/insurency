from sqlalchemy import create_engine
from sqlalchemy.orm import Session


engine = create_engine("sqlite:///library_homework_lesson21.db")
session_create = Session(engine)