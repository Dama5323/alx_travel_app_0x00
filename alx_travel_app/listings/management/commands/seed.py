from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        sample_data = [
            {
                "title": "Beachside Bungalow",
                "description": "Relax by the ocean.",
                "location": "Mombasa",
                "price_per_night": 120.00,
            },
            {
                "title": "Mountain Retreat",
                "description": "Enjoy the cool highlands.",
                "location": "Nyeri",
                "price_per_night": 90.00,
            },
            {
                "title": "Nairobi City Apartment",
                "description": "In the heart of the capital.",
                "location": "Nairobi",
                "price_per_night": 150.00,
            },
        ]

        for data in sample_data:
            listing, created = Listing.objects.get_or_create(
                title=data['title'],
                defaults=data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created listing: {listing.title}"))
            else:
                self.stdout.write(self.style.WARNING(f"Listing already exists: {listing.title}"))
