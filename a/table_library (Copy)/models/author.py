from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from table_library.models.create_session import Base


class Author(Base):
    __tablename__ = 'authors'

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)

    # books:Mapped[List[Any]] = relationship('Book',backref='author', lazy='joined',
    #                                          cascade='all, delete-orphan')

    def __repr__(self):
        return f'{self.first_name} {self.last_name}'

    def __getitem__(self, item):
        return getattr(self, item)

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
