# Generated by Django 4.1 on 2022-08-26 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Entrega", "0002_familia2_delete_familia"),
    ]

    operations = [
        migrations.CreateModel(
            name="familia",
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
                ("Nombre", models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(name="familia2",),
    ]
