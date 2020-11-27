from flask import Flask, request 
import pandas as pd 
import sqlite3
app = Flask(__name__) 
conn = sqlite3.connect("data/chinook.db")


#home root
@app.route('/')
def homepage():
    return str(100*100) #"Hello world"

# mendapatkan buku (static - no variable)
@app.route('/ambil_buku')
def ambilbuku():
    data = pd.read_csv('data/books_c.csv')
    return data.to_json()

@app.route('/ambil_pulsar')
def ambilpulsar():
    data = pd.read_csv('data/pulsar_stars.csv')
    return data.to_json()

# buat endpoint yang menghasilkan hasil crosstabulasi 
@app.route('/top_rating_book')
def topratingbook ():
    books = pd.read_csv('data/books_c.csv')
    condition = books['average_rating'] == 5
    books = books[condition]
    return books.to_json()

@app.route('/get_author/<name>')
def getauthor(name):
    author = name
    books = pd.read_csv('data/books_c.csv')
    condition = books['authors'] == author
    books = books[condition]
    return books.to_json()

# mendapatkan keseluruhan data dari <data_name> (dynamic - with variable)
@app.route('/data/get/<data_name>', methods=['GET']) 
def get_data(data_name): 
    data = pd.read_csv('data/' + str(data_name))
    return (data.to_json())
 


# mendapatkan data dengan filter nilai <value> pada kolom <column>
@app.route('/data/get/equal/<data_name>/<column>/<value>', methods=['GET']) 
def get_data_equal(data_name, column, value): 
    data = pd.read_csv('data/' + str(data_name))
    mask = data[column] == value
    data = data[mask]
    return (data.to_json())

if __name__ == '__main__':
    app.run(debug=True, port=5000) 