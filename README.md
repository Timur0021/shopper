# Karte

A simple Django web application for displaying categories and city-related content.

## Features

* Django 6
* MySQL database
* Bootstrap 5 UI
* Category listing page
* Responsive design
* Static assets management (CSS/SCSS)

## Requirements

* Python 3.12+
* MySQL 8+
* pip
* virtualenv

## Installation

### Clone the repository

```bash
git clone <repository-url>
cd karte
```

### Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment

Update the database settings in `karte/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'karte',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

### Run migrations

```bash
python manage.py migrate
```

### Start the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## Project Structure

```text
karte/
├── karte/          # Project configuration
├── main/           # Main application
├── static/         # CSS, images, and other assets
├── manage.py
└── README.md
```

## Technologies

* Python
* Django
* MySQL
* Bootstrap 5
* HTML/CSS

## License

This project is created for educational purposes.
