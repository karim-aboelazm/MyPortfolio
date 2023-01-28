# Generated by Django 4.1.1 on 2023-01-25 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0007_students"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cart",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("total", models.PositiveIntegerField(default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "student",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="portfolio.students",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CourseOrder",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ordered_by", models.CharField(max_length=200)),
                ("phone_num", models.CharField(max_length=15)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("subtotal", models.PositiveIntegerField()),
                ("total", models.PositiveIntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "payment_method",
                    models.CharField(
                        choices=[("Paypal", "Paypal"), ("Credit Card", "Credit Card")],
                        default="Paypal",
                        max_length=20,
                    ),
                ),
                (
                    "payment_completed",
                    models.BooleanField(blank=True, default=False, null=True),
                ),
                (
                    "cart",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="portfolio.cart"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CartCourse",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("rate", models.PositiveIntegerField()),
                ("subtotal", models.PositiveIntegerField()),
                (
                    "cart",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="portfolio.cart"
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="portfolio.courses",
                    ),
                ),
            ],
        ),
    ]