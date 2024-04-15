from flask import Flask, request, jsonify
from service import BookService
from fastapi import Depends
from database import Base, engine
from sqlalchemy.orm import Session
import model
from model import Book

from service import BookService
from database import SessionLocal
from flasgger import Swagger
from flasgger import swag_from
model.Base.metadata.create_all(bind=engine)
import json
app = Flask(__name__)
swagger = Swagger(app)
book_service = BookService()




@app.route('/books', methods=['POST'])
@swag_from('swagger/add_book.yml')
def add_book():
    data = request.json
    new_book  = Book(title=data['title'], author=data['author'], isbn=data['isbn'], price=data['price'])
    # json_data = request.get_json()
    # print(type(json_data))
    # new_book = Book(**json_data)
    db = SessionLocal()
    try:
        result = book_service.add_book(new_book, db)
        return result
    finally:
        db.close()


@app.route('/books/<int:bookid>', methods=['DELETE'])
@swag_from('swagger/delete_book.yml')
def delete_book(bookid: int):
    db = SessionLocal()
    try:
       
        result = book_service.delete_book(db, bookid)
        return result
    finally:
        db.close()

@app.route('/books',methods=['GET'])
@swag_from('swagger/book_get.yml')
def get_all():
    db = SessionLocal()
    try:
         
         result = book_service.get_all(db)
         return result
    finally:
        db.close()

@app.route('/books/<int:bookid>',methods=['GET'])
@swag_from('swagger/get_book_by_id.yml')
def get_book_by_id(bookid: int):
    db = SessionLocal()
    try:
        
        result = book_service.get_book_by_id(db, bookid)
        return result
    finally:
        db.close()

@app.route('/books/<int:bookid>',methods=['PUT'])  
@swag_from('swagger/update_book.yml')
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
@swag_from('swagger/search_book.yml')
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
    app.run(debug=False, host='0.0.0.0', port=5001)