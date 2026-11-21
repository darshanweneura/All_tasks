from sqlalchemy import create_engine, String, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_engine("sqlite:///C:/Users/Deval/OneDrive/Documents/GitHub/Python-Tasks/flask_project/Demo/student.db")

class Base(DeclarativeBase):
    pass


class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    age: Mapped[int] = mapped_column(Integer)
    course: Mapped[str] = mapped_column(String(100))


Base.metadata.create_all(engine)
