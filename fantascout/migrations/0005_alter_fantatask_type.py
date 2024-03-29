# Generated by Django 4.1 on 2024-01-13 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fantascout", "0004_fantatask_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fantatask",
            name="type",
            field=models.CharField(
                choices=[
                    ("AM", "Abilità Manuale"),
                    ("PP", "Progressione Personale"),
                    ("SS", "Spirito di Servizio"),
                    ("SP", "Spirito di Pattuglia"),
                    ("AW", "Vincitore di giochi"),
                    ("ST", "Stile"),
                ],
                max_length=2,
            ),
        ),
    ]
