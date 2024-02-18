from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("sqlite:///book.db")
Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer(), primary_key=True)
    title = Column(String())
    isbn = Column(Integer())
    publication_date = Column(String())
    description = Column(String())
    publisher = Column(String())
    language = Column(String())
    pages_count = Column(Integer())
    rating = Column(Integer())

#create an engine
engine = create_engine('sqlite:///library.db')
Base.metadata.create_all(engine)    