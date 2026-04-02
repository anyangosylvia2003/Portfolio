from django.contrib import admin
from .models import Project, ContactMessage, Profile, Skill

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')
    
    def has_add_permission(self, request):
        # Limit to only one profile record
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)
    search_fields = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'technologies', 'created_at')
    search_fields = ('name', 'technologies')
    list_filter = ('created_at',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
    readonly_fields = ('name', 'email', 'message', 'created_at')
