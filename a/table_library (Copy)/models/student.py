import csv
from typing import List, Any

from sqlalchemy import select, Boolean, String
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import Mapped, relationship, mapped_column

from table_library.models.create_session import Base, sessions


class Student(Base):
    __tablename__ = 'students'

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    phone: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    average_score: Mapped[float] = mapped_column(nullable=False)
    scholarship: Mapped[bool] = mapped_column(Boolean, nullable=False)

    books: Mapped[List[Any]] = relationship('ReceivingBook',
                                            back_populates='student',
                                            cascade='all, delete-orphan',
                                            lazy='joined')
    receive = association_proxy('student', 'book')

    @classmethod
    def get_student_by_scholarship(cls):
        students = sessions.execute(select(Student) \
                                    .filter(Student.scholarship == True)
                                    ).unique().all()
        student_list = []
        for student in student_list:
            student_list.append(student[0].to_json())
        sessions.commit()
        sessions.close()
        return student_list

    @classmethod
    def get_status_by_high_avarege_ckore(cls, input_score):
        # список студентов с балом выше чем input_score
        students = sessions.query(Student).filter(Student.average_score > input_score).all()
        students_list = []
        for student in students:
            students_list.append(student.to_json())
        sessions.commit()
        sessions.close()
        return students_list

    @classmethod
    def read_csv(cls,student):
        with open(student,newline='')as csvfile:
            reader = csv.DictReader(csvfile,delimiter=';')
            student_list = [student for student in reader]
        sessions.bulk_insert_mappings(Student, student_list)
        return

    def __repr__(self):
        return self.first_name + " " + self.last_name

    def __getitem__(self, item):
        return getattr(self, item)

    def to_json(self):
        return {c.name: f'{getattr(self, c.name)}' for c in self.__table__.columns}
