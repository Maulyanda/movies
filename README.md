<!-- omit in toc -->
# Example CRUD Movie with Framework Django and Database MySQL

## Documentation API
https://documenter.getpostman.com/view/19416331/2s8YzZQKUK

## Requirements

Python 3.7 or later

## Installation

Install Package, run ```pip install -r requirements.txt```

Migrate Database, run ```python manage.py migrate```

## Usage

#### Connect Database

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'your_host',
        'PORT': '3306',
    }
}
```

## Tests

### Running the Test

Make sure the the code passes all tests.

Run the test:

```
python manage.py runserver
```