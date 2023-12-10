from flask import Flask, jsonify, request

app=Flask(__name__)

# simple data
books = [
    {'id':1, 'name':'sandip','author':'sandipk'},
    {'id':2, 'name':'sapna','author':'sugga'},
    {'id':3, 'name':'sandhya','author':'di'},
    {'id':4, 'name':'vivek','author':'bigb'}
]

@app.route('/', methods=['GET'])
def greet():
    return jsonify("hello World")

@app.route('/books', methods=['GET'])
def get_all_books():
    return jsonify({'books':books})

@app.route('/book/<int:book_id>', methods=['GET'])
def get_specific_book(book_id):
    for book in books:
        if book_id == book['id']:
            return jsonify({'book':book})
    else:
        return jsonify({'message':'book not found'}), 404

# post - create a book
@app.route('/create', methods=['POST'])
def create_book():
    print(request)
    name=request.json.get('name')
    author=request.json.get('author')
    id = len(books)+1
    new_book={'id': id,'name': name, 'author': author}
    books.append(new_book)
    return jsonify({'message': 'book created', 'book': new_book}), 201

# Put - update a book
@app.route('/update/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    print(request.json)
    updated_name=request.json.get('name')
    for book in books:
        if book_id == book['id']:
            book['name']=updated_name
            return jsonify({'message':'book update successful','book': book})
    return jsonify({'message':'book not found'}), 404

# Delete - delete a book
@app.route('/delete/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    for book in books:
        if book_id == book['id']:
            books.remove(book)
            return jsonify({'message':'book deleted'})

if __name__ == "__main__":
    app.run(debug=True)