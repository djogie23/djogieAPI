# p4da-capstone-api
This is Algoritma's Python for Data Analysis Capstone Project. This project aims to create a simple API to fetch data from Heroku Server. 

As a Data Scientist, we demand data to be accessible. And as a data owner, we are careful with our data. As the answer, data owner create an API for anyone who are granted access to the data to collect them. In this capstone project, we will create Flask Application as an API and deploy it to Heroku Web Hosting. 

We provide a brief guideline to create the API and how to Deploy in `Capstone Guideline.ipynb` using Bahasa Indonesia. 

You can check the rubrics on rubrics folder
___
## Dependencies : 
- Pandas    (pip install pandas)
- Flask     (pip install flask)
- Gunicorn  (pip install gunicorn)
___
## Goal 
- Create Flask API App
- Deploy to Heroku
- Build API Documentation of how your API works
- Implements the data analysis and wrangling behind the works

___
We have deployed a simple example on : https://djogieapi.herokuapp.com
Here's the list of its endpoints: 
```
1. / , method = GET
Base Endpoint, returning welcoming string value. 

2. /Stock2018 , method = GET, static
Return all closing price stock for Apple, Google and Facebook in full-year 2018.
Blank data in weekend/ holiday already filled with missing value operation. 
    
3. /customer_data, method = GET, static
Return all total customer spending data by using groupby operation from chinook.db

4. /daily_invoices, method = GET, static
Return total number of daily invoices for respective countries by using frequencies analysis (crosstab)

5. /daily_data/<name>, method = GET. dynamic
Return daily transaction data from Monday to Sunday. Date operation was used to get day name from date data.
example: /daily_data/Friday

6. /music/<name>, method = GET, dynamic
Return musical genre popularity in all country. Four tables were joined and categorical operation applied to get this query.
List of genre category: 
       'Rock', 'Jazz', 'Metal', 'Alternative & Punk', 'Rock And Roll',
       'Blues', 'Latin', 'Reggae', 'Pop', 'Soundtrack', 'Bossa Nova',
       'Easy Listening', 'Heavy Metal', 'R&B/Soul', 'Electronica/Dance',
       'World', 'Hip Hop/Rap', 'TV Shows', 'Science Fiction',
       'Sci Fi & Fantasy', 'Drama', 'Comedy', 'Alternative', 'Classical'
example: /music/Latin
```

If you want to try it, you can access (copy-paste it) : 
- https://djogieapi.herokuapp.com
- https://djogieapi.herokuapp.com/Stock2018
- https://djogieapi.herokuapp.com/customer_data
- https://djogieapi.herokuapp.com/daily_invoices
- https://djogieapi.herokuapp.com/daily_data/Tuesday
- https://djogieapi.herokuapp.com/music/Pop
- and so on, just follow the endpoint's pattern
