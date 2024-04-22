# from sqlalchemy import Column, ForeignKey, Integer
# from sqlalchemy.orm import relationship
# from database import Base
# from model import Book

# class Rating(Base):
#     __tablename__ = 'ratings'

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
#     rating = Column(Integer)

  
#     book = relationship('Book', back_populates='ratings')

#     def __init__(self, book_id: int, rating: int):
#         self.book_id = book_id
#         self.rating = rating
