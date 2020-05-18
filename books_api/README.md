# books-api

API to manipulates books and authors information. Written using Python 3.7, Django and Django REST framework along with a few dependencies - check Pipfile on the root directory for more info.

The app is deployed on Heroku with the URL `https://work-at-olist-kenny.herokuapp.com/`.


# API routes

**1. List all authors on the database:**
```
# METHODS ALLOWED: GET
https://work-at-olist-kenny.herokuapp.com/authors/
```

You can perform a query of author by name, like the following:
```
https://work-at-olist-kenny.herokuapp.com/authors/?name=luciano
```

**2. CRUD for Books**

To create or list all books available, you can use de route below:
```
# METHODS ALLOWED: GET, POST
https://work-at-olist-kenny.herokuapp.com/books/
```
 - 2.1 Use the POST method sending the json data - name, edition, publication year and array of authors -, only name is required.
```
{
    "name": "Harry Potter and the Philosopher's Stone",
    "edition": "3",
    "publication_year": 2000,
    "authors": [
        6
    ]
}
```

In order to view one specific book, update or delete one, use the following URL - where id is the books id on the database:
```
# METHODS ALLOWED: GET, DEL, PUT, PATCH
https://work-at-olist-kenny.herokuapp.com/books/{id}
```
- 2.2 For viewing and deleting, you shall only provide the book id on the get parameter and the proper request method.
- 2.3 For updating entirely or partially, use the same json structure described on 2.1 topic.


# Quick setup locally

The project use pipenv as virtual environment provider, on the root directory, start it with:
```
# Creates environment and install dependencies
pipenv install

# Enter into the environment
pipenv shell
```

Run database migration and create superuser:
```
python manage.py migrate
python manage.py createsuperuser
```

The app is all set, the standard Django's admin dashboard `http://localhost:8080/admin` is active as well as the browsable view from Django REST framework `http://localhost:8080/`.
```
python manage.py runserver
```

**Write to the Authors table from csv file**

There is a custom django command `import_authors` for writing on authors table, after the migration, run:
```
python manage.py import_authors file_path.csv
```


# Perform API tests

Inside the `core` app, there is a basic api views test, to perform locally inside your virtual environment, run:
```
python manage.py test
```
