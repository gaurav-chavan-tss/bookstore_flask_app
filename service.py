from database import SessionLocal
from fastapi import Depends
from model import Book
from repository import BookRepository
from flask import jsonify

from sqlalchemy.orm import Session

class BookService:

    def __init__(self):
        self.book_repo = BookRepository()

    def add_book(self,book:Book,db:Session):
        present_book = self.book_repo.get_book_by_isbn(db,book.isbn)
        if present_book is not None:
            return {"code":401,"msg":"ISBN should be unique."}

        new_book = Book(title=book.title,author=book.author,isbn=book.isbn,price=book.price)
        book_temp= self.book_repo.add_book(new_book,db)
        if book_temp is None:
            return {"code":500, "msg":"Book can not be added."}

        book_data = {
            'id': new_book.id,
            'title': new_book.title,
            'author': new_book.author,
            'isbn': new_book.isbn,
            'price': new_book.price
        }
        return {"code": 201, "msg": "Created Successfully", "data": book_data}

    def delete_book(self,bookid:int,db:Session):
        book_temp = self.book_repo.delete_book(bookid,db)
        if book_temp is None:
            return {"code":500, "msg":"Book not found"}
        book_data = {
            'title': book_temp.title,
            'author':  book_temp.author,
            'isbn':  book_temp.isbn,
            'price':  book_temp.price
        }
        return {"code": 201, "msg": "Book deleted Successfully", "data": book_data}


    def get_all(self,db:Session):
        
        books = self.book_repo.get_all(db)
        if len(books) is 0:
            return {"code":404,"msg":"No books found"}

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

        return {"code":201,"msg":"Books found","data": books_data}

    def get_book_by_id(self,db:Session,bookid:int):
        book_temp = self.book_repo.get_book_by_id(db,bookid)
        if book_temp is None:
            return {"code":500, "msg":"Book not found"}
        book_data = {
            'id' : book_temp.id,
            'title': book_temp.title,
            'author':  book_temp.author,  
            'isbn':  book_temp.isbn,
            'price':  book_temp.price
        }
        return {"code": 201, "msg": "Book found successfully", "data": book_data}

    def update_book(self,db:Session,bookid:int,book:Book):
        duplicate_book = self.book_repo.get_book_by_isbn(db,book.isbn)
        if duplicate_book is not None:
            return {"msg":"Book with this isbn already exists."}
        book_temp = self.book_repo.update_book(db,bookid,book)
        if book_temp is None:
            return {"code":500, "msg":"Book not found"}
        book_data = {
            'title': book_temp.title,
            'author':  book_temp.author,
            'isbn':  book_temp.isbn,
            'price':  book_temp.price
        }
        return {"code": 201, "msg": "Book updated successfully", "data": book_data}

    def search_book(self,db:Session,title:str):
        books_found = self.book_repo.search_book(db,title)
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

        return {"code":201,"msg":"Books found","data": books_data}
        


        