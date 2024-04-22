from database import SessionLocal
from fastapi import Depends
from model import Book
# from model2 import Rating
# from model2 import Rating
from repository import BookRepository
from flask import jsonify

from sqlalchemy.orm import Session

class BookService:

    def __init__(self):
        self.book_repo = BookRepository()

    def add_book(self,book:Book,db:Session):
        present_book = self.book_repo.get_book_by_isbn(db,book.isbn)
        if present_book is not None:
            return {"msg":"ISBN should be unique."}

        new_book = Book(title=book.title,author=book.author,isbn=book.isbn,price=book.price)
        book_temp= self.book_repo.add_book(new_book,db)
        if book_temp is None:
            return {"msg":"Book can not be added."}

        book_data = {
            'id': new_book.id,
            'title': new_book.title,
            'author': new_book.author,
            'isbn': new_book.isbn,
            'price': new_book.price
        }
        return {"msg": "Created Successfully", "data": book_data}

    def delete_book(self, db: Session,bookid: int):
        existing_book = self.book_repo.get_book_by_id(db,bookid)
        if existing_book is None:
            return {"msg": "Book with the given ID not found."}
            
        deleted_book = self.book_repo.delete_book(db,bookid)
        if deleted_book is None:
            return {"msg": "Failed to delete book"}

        book_data = {
            'title': deleted_book.title,
            'author': deleted_book.author,
            'isbn': deleted_book.isbn,
            'price': deleted_book.price
        }
        return {"msg": "Book deleted successfully", "data": book_data}



    def get_all(self,db:Session,page,page_size,sort_by,order_by):
        
        books = self.book_repo.get_all(db,page,page_size,sort_by,order_by)
        if len(books) is 0:
            return {"msg":"No books found"}

        books_data = []
        for book in books:
            book_data = {
            'id' : book.id,
            'title': book.title,
            'author': book.author,
            'isbn': book.isbn,
            'price': book.price
            }
            books_data.append(book_data)

        return {"msg":"Books found","data": books_data}

    def get_book_by_id(self,db:Session,bookid:int):
        book_temp = self.book_repo.get_book_by_id(db,bookid)
        if book_temp is None:
            return {"msg":"Book not found"}
        book_data = {
            'id' : book_temp.id,
            'title': book_temp.title,
            'author':  book_temp.author,  
            'isbn':  book_temp.isbn,
            'price':  book_temp.price
        }
        return {"msg": "Book found successfully", "data": book_data}

    # def update_book(self,db:Session,bookid:int,book:Book):
    #     bookavail = self.book_repo.get_book_by_id(db,bookid)
    #     if bookavail is None:
    #         return {"msg":"Book with given ID not found."}

    #     duplicate_book = self.book_repo.get_book_by_isbn(db,book.isbn)
    #     if duplicate_book is not None:
    #         return {"msg":"Book with this isbn already exists."}


    #     book_temp = self.book_repo.update_book(db,bookid,book)
    #     if book_temp is None:
    #         return {"msg":"Book update failed."}
        
    #     book_data = {
    #         'title': book_temp.title,
    #         'author':  book_temp.author,
    #         'isbn':  book_temp.isbn,
    #         'price':  book_temp.price
    #     }
    #     return {"code": 201, "msg": "Book updated successfully", "data": book_data}

    def search_book(self,db:Session,search_term:str,search_item:str,page,page_size,sort_by,order_by):
        books_found = self.book_repo.search_book(db,search_term,search_item,page,page_size,sort_by,order_by)
        if not books_found:
            return {"code":500,"msg":"Books not found"}
        books_data = []
        for book in books_found:
            book_data = {
            'id' : book.id,
            'title': book.title,
            'author': book.author,
            'isbn': book.isbn,
            'price': book.price
            }
            books_data.append(book_data)

        return {"msg":"Books found","data": books_data}
    

    def update_book(self, db: Session, bookid: int, **kwargs):
        bookavail = self.book_repo.get_book_by_id(db, bookid)
        if bookavail is None:
            return {"msg": "Book with given ID not found."}

        if 'isbn' in kwargs:
            duplicate_book = self.book_repo.get_book_by_isbn(db, kwargs['isbn'])
            if duplicate_book and duplicate_book.id != bookid:
                return {"msg": "Book with this isbn already exists."}

        book_temp = self.book_repo.update_book(db, bookid, **kwargs)
        if book_temp is None:
            return {"msg": "Book update failed."}
        
        book_data = {
            'title': book_temp.title,
            'author':  book_temp.author,
            'isbn':  book_temp.isbn,
            'price':  book_temp.price
        }
        return {"msg": "Book updated successfully", "data": book_data}
    

    # def add_rating(self,db:Session,rating:Rating):
    #     new_rating = Rating(book_id=rating.book_id,rating=rating.rating)
    #     rating_added= self.book_repo.add_book(new_rating,db)
    #     if rating_added is None:
    #         return {"msg":"Book can not be added."}

    #     rating_data = {
    #         'id': new_rating.id,
    #         'book_id': new_rating.book_id,
    #         'rating':new_rating.rating
            
    #     }
    #     return {"msg": "Rating added Successfully", "data": rating_data}

        


        