from sqlalchemy import select, Boolean, String
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import Mapped, relationship, mapped_column
from module_21_orm_2.tren.models.base import Base

from module_21_orm_2.tren.models.create_engine import session_create

class Student(Base):
    __tablename__ = 'students'
    #
    # first_name: Mapped[str_50]
    # last_name: Mapped[str_50]
    # phone: Mapped[str_50]
    # email: Mapped[str_50]
    # average_score: Mapped[int | None]
    # scholarship: Mapped[bool | None]

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(30), nullable=False)
    last_name: Mapped[str] = mapped_column(String(30), nullable=False)
    phone: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    average_score: Mapped[float] = mapped_column(nullable=False)
    scholaraship: Mapped[Boolean] = mapped_column(Boolean, nullable=False)

    books = relationship('ReceivingBook', back_populates='student')

    student_receiving_books = relationship("ReceivingBook",
                                           back_populates="student_with_book",
                                           cascade="all, delete-orphan",
                                           lazy="joined")
    receive = association_proxy("student_receiving_books", "book")

    @classmethod
    def get_student_by_scholarship(cls):
        with (session_create() as session):
            students = session.execute(select(Student) \
                                       .filter(Student.scholarship == True)
                                       ).unique().all()
            student_list = []
            for student in student_list:
                student_list.append(student[0].to_json())
            return student_list

    @classmethod
    def get_status_by_high_avarege_ckore(cls, input_score):
        # список студентов с балом выше чем input_score
        with session_create() as session:
            students = session.query(Student).filter(Student.average_score > input_score).all()
            students_list = []
            for student in students:
                students_list.append(student.to_json())
            return students_list

    def __repr__(self):
        return self.first_name + " " + self.last_name

    def __getitem__(self, item):
        return getattr(self, item)

    def to_json(self):
        return {c.name: f'{getattr(self, c.name)}' for c in self.__table__.columns}

