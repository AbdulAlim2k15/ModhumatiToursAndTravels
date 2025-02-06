from django.shortcuts import render
from .models import PopularLocation
from .models import TeamMember
from itertools import groupby
from operator import itemgetter
from operator import attrgetter

def home_view(request):
    # Fetch all popular locations from the database
    popular_locations = PopularLocation.objects.all()
    
    # Pass the data to the template
    context = {
        'popular_locations': popular_locations,
    }
    return render(request, 'tours/home.html', context)

def about_view(request):
    return render(request, 'tours/about.html')

def service_view(request):
    return render(request, 'tours/services.html')



def destination_view(request):
    # Fetch all popular locations and order them by region
    popular_locations = PopularLocation.objects.all().order_by('region')
    
    # Group locations by region
    grouped_locations = {
        region: list(locations)
        for region, locations in groupby(popular_locations, key=attrgetter('region'))
    }
    
    return render(request, 'tours/destination.html', {'grouped_locations': grouped_locations})

# def team_view(request):
#     members = TeamMember.objects.all()  # Fetch all team members from DB
#     context = {
#         'team_members': members,
#     }
#     return render(request, 'tours/team_members.html', context)

def team_view(request):
    members = TeamMember.objects.all().order_by('designation')  # Order by designation
    grouped_members = {
        designation: list(group)
        for designation, group in groupby(members, key=lambda x: x.designation)
    }
    
    context = {
        'grouped_members': grouped_members,
    }
    return render(request, 'tours/team_members.html', context)

def visa_view(request):
    return render(request, 'tours/visa.html')

def contact_view(request):
    return render(request, 'tours/contact.html')