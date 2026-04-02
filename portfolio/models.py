from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100, default="Owiye Sylvia")
    title = models.CharField(max_length=100, default="Full-stack Developer")
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Profile"

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('Programming', 'Programming Languages'),
        ('Frontend', 'Frontend Development'),
        ('Backend', 'Backend Development'),
        ('Databases', 'Databases'),
        ('Collaboration', 'Version Control & Collaboration'),
        ('Tools', 'Tools & Technologies'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.category})"

    class Meta:
        ordering = ['category', 'name']

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=200, help_text="Comma-separated list of technologies")
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"

    class Meta:
        ordering = ['-created_at']
