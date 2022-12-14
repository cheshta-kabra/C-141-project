from flask import Flask,jsonify,request
import csv 
all_books=[]
with open('articles.csv',encoding="utf8") as f:
    reader=csv.reader(f)
    data=list(reader)
    all_books=data[1:]
liked=[]
disliked=[]
did_not_read=[]
app=Flask(__name__)

@app.route('/get-book')
def get_book():
    return jsonify({
        'data':all_books[0],
        'status':'success'
    })

@app.route('/liked-books',methods=['POST'])
def liked_book():
    book=all_books[0]
    all_books=all_books[1:]
    liked.append(book)
    return jsonify({
        'status':'success'
    })
@app.route('/disliked-books',methods=['POST'])
def disliked_book():
    book=all_books[0]
    all_books=all_books[1:]
    disliked.append(book)
    return jsonify({
        'status':'success'
    })
@app.route('/did-not-read-books',methods=['POST'])
def did_not_read_book():
    book=all_books[0]
    all_books=all_books[1:]
    did_not_read.append(book)
    return jsonify({
        'status':'success'
    })
if __name__== '__main__':
    app.run()
