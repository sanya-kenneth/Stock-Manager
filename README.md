# Store-Manager

[![Build Status](https://travis-ci.org/sanya-kenneth/Store-Manager.svg?branch=ft-API)](https://travis-ci.org/sanya-kenneth/Store-Manager)  [![Coverage Status](https://coveralls.io/repos/github/sanya-kenneth/Store-Manager/badge.svg?branch=ft-API)](https://coveralls.io/github/sanya-kenneth/Store-Manager?branch=ft-API)

## About

Store Manager is a web application that helps store owners manage sales and product inventory records. This application is meant for use in a single store

## Features

* Admin can add a product

* Admin/store attendant can get all products

* Admin/store attendant can get a specific product

* Store attendant can add a sale order

* Admin can get all sale order records

## Getting Started

Clone the project from this [link]()

## Prerequisites

* A computer with an operating system (Linux, MacOS or Windows can do the job)
  Python 3.6
* Pytest or any other preffered python tesing tool
* Postman to test the API endpoints
* A preffered text editor
* Git to keep track of the different project branches

## Installing

Clone the project using this link => 

Open your terminal or command prompt for windows users

Type

```
$ cd Store-Manager
$ git checkout ft-API
$ virtualenv venv
$ pip install -r requirements.txt
$ python run.py
```

## Deployment

> The API is hosted on Heroku. Use the link below to navigate to it.

## Testing the Api

Run the command below to install pytest in your virtual environment

`$ pip install pytest`

Run the tests

`$ pytest -v`

## Endpoints

| Endpoint          | Functionality |
| --------          |     --------- |
| `GET /api/v1/products` | Fetch all products |
| `GET /api/v1/products/<product_id>` | Fetch a specific product |
| `GET /api/v1/sales` | Get all sale records |
| `GET /api/v1/sales/<saleId>` | Fetch a single sale record |
| `POST /api/v1/products` | Create a product |
| `POST /api/v1/sales` | Create a sale order |
| `POST /api/v1/users` | Create a store attendant account |
| `POST /api/v1/users/admin` | Create admin account |
| `POST /api/v1/users/login` | Login store attendant or admin |

## Built With

 Python 3.6
 Flask (A python microframework)

## Tools Used

* Pylint
* Pytest
* Virtual environment

## Authors

Sanya Kenneth

Email  : sanyakenneth@gmail.com

## Acknowledgements

Special thanks goes to Andela for making cohort 13 possible and above all, great thanks to God who makes everything possible.