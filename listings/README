## 📥 Seed Script - seed.py
The seed.py file is a Django custom management command that seeds the database with sample travel listings. It helps developers quickly populate the database with mock data for testing or development purposes.

## 📌 File Location
listings/
└── management/
    └── commands/
        └── seed.py
## 🧩 Features
Adds a predefined set of Listing entries to the database

Uses get_or_create() to avoid duplicate entries

Displays success and warning messages in the terminal

##🚀 Usage
Before running the script, make sure:

All migrations are applied:

#python manage.py migrate
Then run the seeder:

#python manage.py seed
🔁 Sample Listings Created
The following mock listings are added to the database:

Title	Location	Price (USD)
Beachside Bungalow	Mombasa	120.00
Mountain Retreat	Nyeri	90.00
Nairobi City Apartment	Nairobi	150.00

## ✅ Requirements
A Django model Listing must be defined in listings/models.py

Proper app and project setup

All __init__.py files in place to recognize the management command

Django environment must be active

##💡 Tip
You can modify the sample_data list inside seed.py to create custom listings for your own use case.


