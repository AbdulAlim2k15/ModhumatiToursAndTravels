# Modhumati Tours and Travels

A web-based application for Modhumati Tours and Travels to showcase services, destinations, visa assistance, and team members, built using Django 5.1.5.

## Features
- **Home Page**: Overview of the travel agency.
- **About Us**: Information about the organization.
- **Services**: List of services offered.
- **Destinations**: Travel destinations available.
- **Visa Assistance**: Details about visa services.
- **Team Members**: Introduction to the team.
- **Contact**: Contact form and information.


## Requirements
To run this project, install the required dependencies:

```ini
Django==5.1.5
pillow==11.1.0

pip install -r requirements.txt

git clone https://github.com/AbdulAlim2k15/ModhumatiToursAndTravels.git
cd ModhumatiToursAndTravels

python -m venv env
env\Scripts\activate  # Windows
source env/bin/activate  # macOS/Linux

pip install -r requirements.txt

cd mtt

python manage.py migrate

python manage.py runserver
Open the project in your browser at: http://127.0.0.1:8000

