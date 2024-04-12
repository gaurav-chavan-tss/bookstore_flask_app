from sqlalchemy.orm import Session
from model import Book
from sqlalchemy import func 
class BookRepository:


  def add_book(self, book: Book,db: Session):
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

  def delete_book(self,db:Session,bookid:int):
    book_to_delete = db.query(Book).filter(Book.id == bookid).first()    
    db.delete(book_to_delete)
    db.commit()
    return book_to_delete

  def get_all(self,db:Session):
    return db.query(Book).all()

  def get_book_by_id(self,db:Session,bookid:int):
    return db.query(Book).filter(Book.id ==  bookid).first()

  def update_book(self,db:Session,bookid:int,book:Book):
    book_get = db.query(Book).filter(Book.id == bookid).first()
    book_get.isbn = book.isbn
    book_get.author= book.author
    book_get.title = book.title
    book_get.price = book.price
    db.commit()
    db.refresh(book_get)
    return book_get

  def search_book(self,db:Session,title:str):
    search_result = db.query(Book).filter(func.lower(Book.title).like(f"%{title.lower()}%")).all()
    return search_result

  def get_book_by_isbn(self,db:Session,isbn:int):
    return db.query(Book).filter(Book.isbn==isbn).first()
        

 