# Resume Processor API

A Django REST API project that extracts candidate information from resume files (PDF/DOCX).

## Features
- Upload resume files (PDF/DOCX support)
- Extract candidate's first name, email, and mobile number
- RESTful API endpoint
- Web interface for easy testing
- PostgreSQL database storage

## Prerequisites
- Python 3.9+
- PostgreSQL
- pip (Python package manager)

## Local Setup Instructions

1. **Clone the repository**
```bash
git clone <your-repository-url>
cd ResumeProcessor
```

2. **Create and activate virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables**
Create a `.env` file in the root directory with:
```
DEBUG=True
SECRET_KEY=your-secret-key-here
DB_NAME=resume_processor_db
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432
```

5. **Setup PostgreSQL database**
- Install PostgreSQL
- Create a database named 'resume_processor_db'
- Update .env with your database credentials

6. **Run migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

7. **Start development server**
```bash
python manage.py runserver
```

## API Documentation

### Extract Resume Information
**Endpoint:** `/api/extract_resume/`
**Method:** POST
**Content-Type:** multipart/form-data

**Request Body:**
- resume: File (PDF/DOCX)

**Response:**
```json
{
    "first_name": "John",
    "email": "john.doe@example.com",
    "mobile_number": "123-456-7890"
}
```

## Testing
1. Visit http://localhost:8000/
2. Upload a resume file using the web interface
3. View extracted information

## Project Structure
```
ResumeProcessor/
├── manage.py
├── requirements.txt
├── .env
├── ResumeProcessor/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── resume/
    ├── models.py
    ├── serializers.py
    ├── services.py
    ├── urls.py
    ├── views.py
    └── templates/
        └── resume/
            └── home.html
```
