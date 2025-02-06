from django.contrib import admin
from .models import PopularLocation
from .models import TeamMember

@admin.register(PopularLocation)
class PopularLocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')  # Fields to display in the admin list view
    search_fields = ('name',)  # Enable search by name



@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'email')
    search_fields = ('name',)  # Enable search by name