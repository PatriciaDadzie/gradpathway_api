import requests
from django.core.management.base import BaseCommand
from catalog.models import University, Programme

API_URL = "https://api.data.gov/ed/collegescorecard/v1/schools"
API_KEY = "YOUR_API_KEY_HERE"  

class Command(BaseCommand):
    help = "Seed U.S. universities and programmes from College Scorecard API"

    def handle(self, *args, **options):
        params = {
            "api_key": API_KEY,
            "fields": "id,school.name,school.city,school.state,school.school_url",
            "per_page": 5
        }

        response = requests.get(API_URL, params=params)
        data = response.json()

        for item in data.get("results", []):
            uni, _ = University.objects.get_or_create(
                name=item.get("school.name"),
                country="United States",
                city=item.get("school.city"),
                website=item.get("school.school_url")
            )
            Programme.objects.get_or_create(
                university=uni,
                title="General Master's Programme",
                discipline="General Studies",
                description="Auto-seeded sample data.",
                duration_months=24,
                tuition=20000,
                min_gpa=3.0,
                mode='on-campus'
            )

        self.stdout.write(self.style.SUCCESS(" U.S. data seeded successfully."))
