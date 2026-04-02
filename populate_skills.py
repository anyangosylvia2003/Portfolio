import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from portfolio.models import Skill

skills_data = [
    # Programming Languages
    ('Python', 'Programming'),
    ('JavaScript (ES6+)', 'Programming'),
    ('HTML5', 'Programming'),
    ('CSS3', 'Programming'),
    
    # Frontend Development
    ('Responsive Web Design', 'Frontend'),
    ('DOM Manipulation', 'Frontend'),
    ('Fetch API', 'Frontend'),
    ('Basic UI/UX Principles', 'Frontend'),
    
    # Backend Development
    ('Django', 'Backend'),
    ('RESTful API Development', 'Backend'),
    ('Authentication & Authorization', 'Backend'),
    ('Form Handling', 'Backend'),
    
    # Databases
    ('SQLite', 'Databases'),
    ('PostgreSQL (basic)', 'Databases'),
    ('Database Design', 'Databases'),
    ('ORM (Django ORM)', 'Databases'),
    
    # Version Control & Collaboration
    ('Git', 'Collaboration'),
    ('GitHub (branching, pull requests)', 'Collaboration'),
    
    # Tools & Technologies
    ('VS Code', 'Tools'),
    ('Postman', 'Tools'),
    ('Virtual Environments', 'Tools'),
    ('Environment Variables (.env)', 'Tools'),
]

def populate():
    # Clear existing skills to avoid duplicates
    Skill.objects.all().delete()
    for name, category in skills_data:
        Skill.objects.create(name=name, category=category)
    print(f"Successfully populated {len(skills_data)} skills.")

if __name__ == '__main__':
    populate()
