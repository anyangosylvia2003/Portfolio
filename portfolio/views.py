from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, Profile, Skill
from .forms import ContactForm

def home(request):
    projects = Project.objects.all()
    profile = Profile.objects.first()
    
    # Group skills by category
    skills_by_category = {}
    for category_code, category_name in Skill.CATEGORY_CHOICES:
        skills = Skill.objects.filter(category=category_code)
        if skills.exists():
            skills_by_category[category_name] = skills
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('home')
    else:
        form = ContactForm()
    
    context = {
        'projects': projects,
        'profile': profile,
        'skills_by_category': skills_by_category,
        'form': form,
    }
    return render(request, 'portfolio/home.html', context)
