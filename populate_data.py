import os
import django
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from portfolio.models import Project, Certification
from django.contrib.auth.models import User

def populate():
    # Create superuser if not exists
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        print("Superuser 'admin' created with password 'admin123'")

    # Add sample projects
    projects = [
        {
            'name': 'E-commerce Platform',
            'description': 'A full-featured e-commerce platform built with Django and React. Includes product management, shopping cart, and payment integration.',
            'technologies': 'Django, React, PostgreSQL, Stripe',
            'github_link': 'https://github.com/johndoe/ecommerce'
        },
        {
            'name': 'Task Management App',
            'description': 'A collaborative task management application with real-time updates using Django Channels.',
            'technologies': 'Django, Redis, Channels, Bootstrap',
            'github_link': 'https://github.com/johndoe/task-manager'
        },
        {
            'name': 'Weather Dashboard',
            'description': 'A weather dashboard that provides real-time weather information and forecasts using OpenWeatherMap API.',
            'technologies': 'Python, Django, API, Chart.js',
            'github_link': 'https://github.com/johndoe/weather-dashboard'
        }
    ]

    for p in projects:
        Project.objects.get_or_create(**p)
    
    print(f"Added {len(projects)} sample projects.")

    # Add sample certifications
    certs = [
        {
            'name': 'AWS Certified Solutions Architect',
            'issuer': 'Amazon Web Services',
            'date_issued': date(2023, 5, 15),
            'link': 'https://aws.amazon.com/verification'
        },
        {
            'name': 'Professional Scrum Master I',
            'issuer': 'Scrum.org',
            'date_issued': date(2022, 11, 10),
            'link': 'https://scrum.org/verification'
        }
    ]

    for c in certs:
        Certification.objects.get_or_create(**c)
    
    print(f"Added {len(certs)} sample certifications.")

if __name__ == '__main__':
    populate()
