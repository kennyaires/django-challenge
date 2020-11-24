Webapp developed using Django for Olist Challenge. Documentation on https://github.com/kennyaires/django-challenge/tree/master/books_api

## Specification

You should implement an application for a library to store book and authors data.

**This application must provide an HTTP REST API to attend the requirements.**

### 1. Receive a CSV with authors and import to database

Given a CSV file with many authors (more than a million), you need to build a command to import the data into the database. The CSV file will have the following format:

```
name
Luciano Ramalho
Osvaldo Santana Neto
David Beazley
Chetan Giridhar
Brian K. Jones
J.K Rowling
```

Each author record in the database must have the following fields:

* id (self-generated)
* name

You need to store the authors' data to complement the book data that will be stored afterward (see item #3).

_Extra tip: If you use Django Framework you can do something like this..._

```
python manage.py import_authors authors.csv
```

### 2. Expose authors' data in an endpoint

This endpoint needs to return a paginated list with the authors' data. Optionally the authors can be searched by name.

### 3. CRUD (Create, Read, Update and Delete) of books

You need to implement these actions in your API:

* Create a book
* Read book's data
* Update book's data
* Delete book's data

Each book record has the fields:

* id (self-generated)
* name
* edition
* publication_year
* authors (more than one author can write a book)

To retrieve a book (in easy mode) we can filter by 4 fields (or a composition of these four):

* name
* publication_year
* edition
* author

But these 4 filters are optional. It must be possible to navigate all the books' data without any filter.

To create a book you need to send this payload (in json format) below:

```
{
 "name": // Name of the book;
 "edition": // Edition number;
 "publication_year": // Publication year of the book;
 "authors": // List of author ids, same ids of previous imported data
}
```

## Project Requirements:

* Provide a working environment with your project (eg. Heroku)
* Application must be written in Python or Go.
* Python
    * Use Python >= 3.5
    * Choose any Python web framework you want to solve the problem
    * Use PEP-8 for code style
    * [Python Coding Style](http://docs.python-guide.org/en/latest/writing/style/)
* Go
    * Go >= 1.10
    * [Effective Go](https://golang.org/doc/effective_go.html)
* Every text or code must be in English
* Write the project documentation containing:
    * Description;
    * Installing (setup) and testing instructions;
    * If you provide a [docker](https://www.docker.com/) solution for setup, ensure it works without docker too.
    * Brief description of the work environment used to run this project (Computer/operating system, text editor/IDE, libraries, etc).
* Provide API documentation (in English);
* Variables, code and strings must be all in English.

## Recommendations

* Write tests! Please make tests ... we appreciate tests <3... tests make the world better;
* Practice the [12 Factor-App](http://12factor.net) concepts;
* Use [SOLID](https://en.wikipedia.org/wiki/SOLID_(object-oriented_design)) design principles;
* Use programming good practices;
* Use [git best practices](https://www.git-tower.com/learn/git/ebook/en/command-line/appendix/best-practices), with clear messages (written in English);
* Be aware when modeling the database;
* Be careful with REST API details. They can bite you!

**Have fun!**
