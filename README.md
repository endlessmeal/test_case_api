# Test api case
Python 3.11.4, Django 5.0.3, djangorestframework 3.14.0

### How to install (Linux/Mac OS)


In the root folder create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate
```
Install all dependencies:
```bash
pip install -r requirements.txt
```

Enter your postgres database and create a new database:

```bash
psql -U your_postgres_user -d postgres
create database your_db_name;
```

There is a .env.example file where you can see an example of creating your .env file. So, create an .env file in the same directory as manage.py located:

```dotenv
SECRET_KEY=your_secret_key
DEBUG=your_debug_option
DB_NAME=your_db_name
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=your_host
DB_PORT=your_port
```

### Migrations
Apply all migrations to your postgres
```bash
python manage.py makemigrations
python manage.py migrate
```
### Launch
```bash
python manage.py runserver
```
### Endpoints
Admin urls starts with admin/ and have endpoints for CRUD operations:
```text
/admin/employees/ [GET, POST, DELETE]
/admin/points_of_sale/ [GET, POST, DELETE]
/admin/visits/ [GET, POST, DELETE]
```
Other urls:
```text
/api/points_of_sale/ [GET]
/api/perform_visit/ [POST] 
```
```bash
python manage.py runserver
```
### Other
If you want to enable djangorestframework browser api for convenient testing just comment out next lines in settings.py:
```python
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}
```