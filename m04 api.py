from flask import Flask, jsonify
app = Flask(__name__)
from flask_sqlalchemy import SQALchemy


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAchemy


class Book(db.Model):
    id = db. Column(db.Integer, primary_key=True)
    bookname = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Columndb.Column(db,String(120))
    publisher = db.Column(db.String(120))

    def __repr__(self)
        return f"{self.name} - {self.publisher} - {self.author}"

@app.route('/')
def index():
    return 'Hello'

@app.rout('/books')
def get_books():
    books = Book.query.all()

    output = []
    for book in books:
        book_data = {'name': book.name, 'author': book.author, 'publisher': book.publisher}

        output.append(book_data)


    return {"books": "output"}

@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify({"name":book.name, "author": book.author})

@app.route('/books'/, methods=['POST'])
def add_book():
    book = Book(name=request.json['name'], 
                author=request.json['author'])
                
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}

@app.route('/books/<id>', methods=['DELETE'])
def delete_book():
    book = Book.query.get(id)
    if book is None:
        return{"error": "404"}
    db.session.delete(book)
    db.session.commit()
    return {"messag": "HA"}
