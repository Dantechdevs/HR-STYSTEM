# Django Admin Dashboard

![Dashboard Preview]<img width="958" alt="image" src="https://github.com/user-attachments/assets/3109f123-8d12-40ab-bb86-40a3579f3717" />


A full-stack admin dashboard built with Django backend and Bootstrap/jQuery frontend.

## Features

### Backend (Django)
- Custom admin interface with dashboard analytics
- Role-based authentication system
- RESTful API endpoints (DRF)
- PostgreSQL database integration
- Automated report generation
- CRUD operations for employee management

### Frontend
- Responsive Bootstrap 5 layout
- Interactive charts with Chart.js
- Real-time updates with jQuery AJAX
- Dynamic form validation
- Data tables with sorting/filtering
- Toast notifications system

## Project Structure
```bash
project-root/
├── core/               # Django main app
│   ├── models/        # Database models
│   ├── views/         # Business logic
│   ├── templates/     # HTML templates
│   └── static/        # CSS/JS assets
├── config/            # Project settings
├── requirements.txt   # Dependencies
└── manage.py          # Django CLI
```

## Installation

### Prerequisites
- Python 3.10+
- PostgreSQL 14+
- Node.js (for frontend dependencies)

```bash
# Clone repository
git clone https://github.com/dantechdevs/django-dashboard.git
cd django-dashboard

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac)
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
nano .env  # Edit database credentials

# Database setup
python manage.py migrate
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# Start development server
python manage.py runserver
```

## Frontend Development
```bash
# Install frontend dependencies
npm install bootstrap jquery @popperjs/core chart.js

# Custom CSS/JS location
core/static/
├── css/
│   └── custom.css
└── js/
    └── main.js
```


## Key Technologies
| Category       | Technologies                          |
|----------------|---------------------------------------|
| Backend        | Django 4.2, Django REST Framework     |
| Frontend       | Bootstrap 5, jQuery 3.7, Chart.js     |
| Database       | PostgreSQL, Django ORM                |
| Deployment     | Gunicorn, Nginx, Docker               |
| Utilities      | Celery, Redis, pytest                 |

## Configuration
```python
# config/settings.py
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'core/static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# .env
DEBUG=True
SECRET_KEY=your-secret-key
DB_NAME=yourdb
DB_USER=youruser
DB_PASSWORD=yourpassword
```

## License
[MIT License](https://opensource.org/licenses/MIT)
