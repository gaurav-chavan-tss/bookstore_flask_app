from flask import Flask, request, jsonify
# from model2 import Rating
# from model2 import Rating
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
    page = request.args.get('page',default=1,type=int)
    page_size = request.args.get('page_size',default=10,type=int)
    sort_by = request.args.get('sort_by',default='id',type=str)
    order_by = request.args.get('order_by',default='asc',type=str)
    db = SessionLocal()
    try:
         
         result = book_service.get_all(db,page,page_size,sort_by,order_by)
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

# @app.route('/books/<int:bookid>',methods=['PUT'])  
# @swag_from('swagger/update_book.yml')
# def update_book(bookid: int):
#     data = request.json
#     new_book  = Book(title=data['title'], author=data['author'], isbn=data['isbn'], price=data['price'])
#     db = SessionLocal()
#     try:
        
#         result = book_service.update_book(db, bookid,new_book)
#         return result
#     finally:
#         db.close()

@app.route('/books/<int:bookid>', methods=['PUT'])  
@swag_from('swagger/update_book.yml')
def update_book(bookid: int):
    data = request.json
    db = SessionLocal()
    try:
        existing_book = db.query(Book).filter(Book.id==bookid).first()
        if existing_book is None:
            return {"msg":"Book not found"}
        update_data={}
        for field in ['title', 'author', 'isbn', 'price']:
            if field in data:
                update_data[field] = data[field]
            else:
                update_data[field] = getattr(existing_book, field)
        result = book_service.update_book(db, bookid, **update_data)
        return result
    finally:
        db.close()

@app.route('/books/search', methods=['GET'])
@swag_from('swagger/search_book.yml')
def search_book():
    search_term = request.args.get('search_term')
    search_item = request.args.get('search_item')
    page = request.args.get('page',default=1,type=int)
    page_size = request.args.get('page_size',default=10,type=int)
    sort_by = request.args.get('sort_by',default='id',type=str)
    order_by = request.args.get('order_by',default='asc',type=str)
    if not search_term or not search_item:
        return jsonify({ "msg": "Bad request: Both 'search_term' and 'search_item' parameters are required"})

    db = SessionLocal()
    try:
     result = book_service.search_book(db, search_term,search_item,page,page_size,sort_by,order_by)
     return result
    finally:
        db.close()

# @app.route('/ratings',methods=['POST'])
# @swag_from('swagger/add_rating.yml')
# def add_rating():
#     data = request.json
#     new_rating  = Rating(book_id=data['book_id'],rating=data['rating'])
#     db = SessionLocal()
#     try:
#         result = book_service.add_rating(db,new_rating)
#         return result
#     finally:
#         db.close()
    

if __name__ == '__main__':
    app.run(debug=False,host="0.0.0.0", port=5000)