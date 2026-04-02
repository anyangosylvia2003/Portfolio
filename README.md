# Django Portfolio Project - Local Setup Guide

This guide will help you set up the portfolio project on your local machine.

## Prerequisites
- Python 3.10 or higher
- `pip` (Python package manager)

## Step 1: Create and Activate a Virtual Environment
It's recommended to use a virtual environment to keep dependencies isolated.

### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

## Step 2: Install Dependencies
Install all required packages using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

## Step 3: Configure Environment Variables
Create a `.env` file in the project root (the same folder as `manage.py`) and add the following:
```env
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
```

## Step 4: Run Migrations
Apply the database migrations:
```bash
python manage.py migrate
```

## Step 5: Create a Superuser (Optional)
To access the admin panel at `/admin`:
```bash
python manage.py createsuperuser
```

## Step 6: Run the Development Server
Start the server:
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000` in your browser to see your portfolio!
