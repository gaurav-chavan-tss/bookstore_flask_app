from sqlalchemy.orm import Session
from model import Book
# from model2 import Rating
from sqlalchemy import func

# from model2 import Rating 
class BookRepository:


  def add_book(self, book: Book,db: Session):
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

  def delete_book(self,db:Session,bookid:int):
    book_to_delete = db.query(Book).filter(Book.id == bookid).first()    
    if book_to_delete:
      db.delete(book_to_delete)
      db.commit()
      return book_to_delete
    return None
    

  def get_all(self,db:Session,page:int,page_size:int,sort_by:str,order_by:str):
    offset = (page-1)*page_size
    sort_field = getattr(Book,sort_by)
    if order_by.lower()=='asc':
      return db.query(Book).order_by(sort_field.asc()).offset(offset).limit(page_size).all()
    else:
      return db.query(Book).order_by(sort_field.desc()).offset(offset).limit(page_size).all()

  def get_book_by_id(self,db:Session,bookid:int):
    return db.query(Book).filter(Book.id ==  bookid).first()

  # def update_book(self,db:Session,bookid:int,book:Book):
  #   book_get = db.query(Book).filter(Book.id == bookid).first()
  #   book_get.isbn = book.isbn
  #   book_get.author= book.author
  #   book_get.title = book.title
  #   book_get.price = book.price
  #   db.commit()
  #   db.refresh(book_get)
  #   return book_get

  def search_book(self, db: Session, search_term: str, search_item: str, page: int, page_size: int, sort_by: str, order_by: str):
    offset = (page - 1) * page_size
    sort_field = getattr(Book, sort_by)
    
    if search_term == 'title':
        query = db.query(Book).filter(func.lower(Book.title).like(f"%{search_item.lower()}%"))
    else:
        query = db.query(Book).filter(func.lower(Book.author).like(f"%{search_item.lower()}%"))
        
    if order_by.lower() == 'asc':
        query = query.order_by(sort_field.asc())
    else:
        query = query.order_by(sort_field.desc())
    
    search_result = query.offset(offset).limit(page_size).all()
    
    return search_result


  def get_book_by_isbn(self,db:Session,isbn:int):
    return db.query(Book).filter(Book.isbn==isbn).first()
  
  def update_book(self, db: Session, bookid: int, **kwargs):
    book_get = db.query(Book).filter(Book.id == bookid).first()
    if book_get:
        for field, value in kwargs.items():
            setattr(book_get, field, value)
        db.commit()
        db.refresh(book_get)
        return book_get
    return None  
  

  # def add_rating(self,db:Session,rating:Rating):
  #   db.add(rating)
  #   db.commit()
  #   db.refresh(rating)
  #   return rating

        

 