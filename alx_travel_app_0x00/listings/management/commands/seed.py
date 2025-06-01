from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = 'Seed database with sample listings'

    def handle(self, *args, **kwargs):
        sample_data = [
            {'title': 'Cozy Cabin', 'description': 'A small cozy cabin in the woods', 'price': 100, 'location': 'Nairobi'},
            {'title': 'Modern Apartment', 'description': 'Luxury apartment in the city center', 'price': 200, 'location': 'Mombasa'},
            {'title': 'Beach House', 'description': 'A beautiful house by the beach', 'price': 300, 'location': 'Diani'}
        ]

        for item in sample_data:
            Listing.objects.create(
                title=item['title'],
                description=item['description'],
                price=item['price'],
                location=item['location'],
                available=random.choice([True, False])
            )

        self.stdout.write(self.style.SUCCESS('✅ Successfully seeded the database with listings.'))
