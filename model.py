from sqlalchemy import Integer,Column,String,Float
from database import Base
from sqlalchemy.orm import relationship 

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True,autoincrement=True)
    title = Column(String)
    author = Column(String)
    isbn = Column(String, unique=True)
    price = Column(Float)


    def __init__(self, title:str,isbn:str,price:float,author:str):
        self.title = title
        self.isbn = isbn
        self.price = price
        self.author = author
