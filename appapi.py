from flask import Flask, request 
import pandas as pd 
import sqlite3
app = Flask(__name__) 

#home root
@app.route('/')
def homepage():
    return "Welcome to djogie23 API!"

# Missing Value and Stack operation - static - Stock Closing Price 2018 in 365 days
@app.route('/Stock2018')
def stock():
    stock = pd.read_pickle('data/stock')
    closingprice = stock['Close']
    year2018 = pd.date_range(start="2018-01-01", end="2018-12-31")
    closingprice = closingprice.reindex(year2018)
    closingprice = closingprice.ffill().bfill().stack()
    return closingprice.to_json()

# Groupby operation - static - Customer Spending
@app.route('/customer_data')
def customer():
    conn = sqlite3.connect("data/chinook.db")
    report = pd.read_sql_query("select Country, Total, FirstName, Lastname, InvoiceDate \
                    from customers \
                    left join invoices \
                    on customers.CustomerId=invoices.CustomerId",conn)
    report['Fullname'] = report['FirstName']+[' ']+report['LastName']
    customerdata = report.groupby('Fullname').Total.sum().sort_values(ascending=False)
    return customerdata.to_json()

# Frequencies analysis (Crosstab) - static - Daily invoices by Country
@app.route('/daily_invoices')
def frequencies():
    conn = sqlite3.connect("data/chinook.db")
    report = pd.read_sql_query("select Country, Total, FirstName, Lastname, InvoiceDate \
                    from customers \
                    left join invoices \
                    on customers.CustomerId=invoices.CustomerId",conn)
    report['InvoiceDate'] = report['InvoiceDate'].astype('Datetime64')
    report['InvoiceDOW'] = report['InvoiceDate'].dt.day_name()
    report = pd.crosstab(
    index=report['Country'],
    columns=report['InvoiceDOW']
    )
    return report.to_json()

# Date operation - dynamic - Daily Transaction Data: Monday to Sunday
@app.route('/daily_data/<name>', methods=['GET'])
def dateoperation(name):
    InvoiceDOW = name
    conn = sqlite3.connect("data/chinook.db")
    report = pd.read_sql_query("select Country, Total, FirstName, Lastname, InvoiceDate \
                    from customers \
                    left join invoices \
                    on customers.CustomerId=invoices.CustomerId",conn)
    report['InvoiceDate'] = report['InvoiceDate'].astype('Datetime64')
    report['InvoiceDOW'] = report['InvoiceDate'].dt.day_name()
    condition = report['InvoiceDOW'] == InvoiceDOW
    report = report[condition]
    return report.to_json()

# Joining 4 table & Categorical Operation - dynamic
@app.route('/music/<name>', methods=['GET'])
def music(name):
    Genre = name
    conn = sqlite3.connect("data/chinook.db")
    music = pd.read_sql_query(
        '''
        SELECT 
        BillingCountry AS Country, genres.Name AS Genre
        FROM invoices 
        LEFT JOIN invoice_items ON invoices.InvoiceId = invoice_items.InvoiceId
        LEFT JOIN tracks ON invoice_items.TrackId = tracks.TrackId 
        LEFT JOIN genres ON tracks.GenreId = genres.GenreId
        ''',conn)
    music[['Country','Genre']] = music[['Country','Genre']].astype('category')
    condition = music['Genre'] == Genre
    music = music[condition]
    return music.to_json()


if __name__ == '__main__':
    app.run(debug=True, port=5000) 