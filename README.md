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
We have deployed a simple example on : https://algo-capstone.herokuapp.com
Here's the list of its endpoints: 
```
1. / , method = GET
Base Endpoint, returning welcoming string value. 

2. /data/get/<data_name> , method = GET
Return full data <data_name> in JSON format. Currently available data are:
    - books_c.csv
    - pulsar_stars.csv 
    
3. /data/get/equal/<data_name>/<column>/<value> , method = GET
Return all <data_nam> where the value of column <column> is equal to <value>
```

If you want to try it, you can access (copy-paste it) : 
- https://algo-capstone.herokuapp.com
- https://algo-capstone.herokuapp.com/data/get/books_c.csv
- https://algo-capstone.herokuapp.com/data/get/pulsar_stars.csv
- https://algo-capstone.herokuapp.com/data/get/equal/books_c.csv/isbn/0439785960
- https://algo-capstone.herokuapp.com/data/get/equal/books_c.csv/authors/J.K. Rowling
- and so on, just follow the endpoint's pattern