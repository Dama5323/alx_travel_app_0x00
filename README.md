# ALX Travel App (0x00) – Database Modeling and Data Seeding

This is the foundational phase of the **ALX Travel App** project. It focuses on designing database models, creating serializers, and populating the database with initial data using a custom management command.

---

## 🚀 Objective

- Define core models for a travel booking app.
- Serialize data for API usage.
- Seed the database with sample listings.

---

## 🛠️ Project Structure

alx_travel_app/
├── listings/
│ ├── models.py # Listing, Booking, Review models
│ ├── serializers.py # DRF serializers for Listing and Booking
│ ├── management/
│ │ └── commands/
│ │ └── seed.py # Seeder command to populate sample data
├── alx_travel_app/
│ └── settings.py # Django settings
├── README.md
└── ...


---

## 📦 Models Overview

### 1. `Listing`
- Destination
- Description
- Price
- Availability

### 2. `Booking`
- Linked to a `Listing`
- User details
- Booking date & status

### 3. `Review`
- Linked to a `Listing`
- User feedback & rating

---

## 🔁 Seed the Database

To populate the database with sample listing data:

```bash
python manage.py seed

This command will insert mock travel listings for testing API endpoints and UI integration.

## 🔌 API Documentation
Swagger and Redoc documentation available:

Swagger: http://localhost:8000/swagger/

Redoc: http://localhost:8000/redoc/

## 🧰 Tech Stack
Python 3

Django

Django REST Framework (DRF)

drf-yasg (for API docs)

## 🤝 Contributing
This project is part of the ALX Backend Development Program. Contributions are welcome via pull requests or forked repos.

## 📬 Contact
Created with 💻 by Damaris
GitHub: @Dama5323
