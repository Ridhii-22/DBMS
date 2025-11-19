from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from tracker.models import Shopkeeper, Customer, Due
from django.db import transaction
from decimal import Decimal
from datetime import date, timedelta

class Command(BaseCommand):
    help = "Seed DB with a shopkeeper, customers and dues."

    def add_arguments(self, parser):
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Remove previously seeded data (seed_* users, shopkeepers, customers, dues).",
        )

    @transaction.atomic
    def handle(self, *args, **options):
        if options["clear"]:
            Due.objects.all().delete()
            Customer.objects.all().delete()
            Shopkeeper.objects.all().delete()
            User.objects.filter(username__startswith="seed_").delete()
            self.stdout.write("Cleared seed data.")

        user, created = User.objects.get_or_create(
            username="seed_shopkeeper",
            defaults={"first_name": "Seed", "email": "seed@example.com"},
        )
        if created:
            user.set_password("password123")
            user.save()

        shop, _ = Shopkeeper.objects.get_or_create(
            user=user,
            defaults={
                "shop_name": "Seed Shop",
                "phone_number": "1234567890",
                "address": "123 Seed Street",
            },
        )

        sample_customers = [
            {"customer_name": "Ramesh", "phone_number": "9876543210", "address": "Village A"},
            {"customer_name": "Suresh", "phone_number": "8765432109", "address": "Village B"},
            {"customer_name": "Geeta", "phone_number": "7654321098", "address": "Town C"},
        ]

        for idx, c in enumerate(sample_customers, start=1):
            cust, _ = Customer.objects.get_or_create(
                shopkeeper=shop,
                customer_name=c["customer_name"],
                defaults={"phone_number": c["phone_number"], "address": c["address"]},
            )
            # create two dues per customer (one pending, one paid)
            Due.objects.get_or_create(
                customer=cust,
                amount=Decimal("100.00") * idx,
                defaults={
                    "description": "Initial pending due",
                    "due_date": date.today() + timedelta(days=7 * idx),
                    "status": "PENDING",
                },
            )
            Due.objects.get_or_create(
                customer=cust,
                amount=Decimal("50.00") * idx,
                defaults={
                    "description": "Already paid example",
                    "due_date": date.today() - timedelta(days=30),
                    "status": "PAID",
                },
            )

        self.stdout.write(self.style.SUCCESS("Seed data created/verified."))
        self.stdout.write("Login: seed_shopkeeper  Password: password123")

