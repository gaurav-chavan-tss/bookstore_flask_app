from flask import Flask, request, jsonify
from service import BookService
from fastapi import Depends
from database import Base, engine
from sqlalchemy.orm import Session
import model
from model import Book
from service import BookService
from database import SessionLocal
model.Base.metadata.create_all(bind=engine)

app = Flask(__name__)

book_service = BookService()




@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    new_book  = Book(title=data['title'], author=data['author'], isbn=data['isbn'], price=data['price'])
    db = SessionLocal()
    try:
        result = book_service.add_book(new_book, db)
        return result
    finally:
        db.close()


@app.route('/books/<int:bookid>', methods=['DELETE'])
def delete_book(bookid: int):
    db = SessionLocal()
    try:
       
        result = book_service.delete_book(db, bookid)
        return result
    finally:
        db.close()

@app.route('/books',methods=['GET'])
def get_all():
    db = SessionLocal()
    try:
         
         result = book_service.get_all(db)
         return result
    finally:
        db.close()

@app.route('/books/<int:bookid>',methods=['GET'])
def get_book_by_id(bookid: int):
    db = SessionLocal()
    try:
        
        result = book_service.get_book_by_id(db, bookid)
        return result
    finally:
        db.close()

@app.route('/books/<int:bookid>',methods=['PUT'])
def update_book(bookid: int):
    data = request.json
    new_book  = Book(title=data['title'], author=data['author'], isbn=data['isbn'], price=data['price'])
    db = SessionLocal()
    try:
        
        result = book_service.update_book(db, bookid,new_book)
        return result
    finally:
        db.close()

@app.route('/books/search',methods=['GET'])
def search_book():
    title = request.args.get('title')
    if not title:
        return jsonify({"code": 400, "msg": "Bad request: 'title' parameter is required"})
    db = SessionLocal()
    try:
        
        result = book_service.search_book(db,title)
        return result
    finally:
        db.close()

if __name__ == '__main__':
    app.run(debug=True, port=5001)