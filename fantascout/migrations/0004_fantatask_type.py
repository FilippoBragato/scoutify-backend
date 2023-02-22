# Generated by Django 4.1 on 2023-02-20 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fantascout", "0003_fantatask_personal"),
    ]

    operations = [
        migrations.AddField(
            model_name="fantatask",
            name="type",
            field=models.CharField(
                choices=[
                    ("AM", "Abilità Manuale"),
                    ("PP", "Progressione Personale"),
                    ("SS", "Spirito di Servizio"),
                    ("SP", "Spirito di Pattuglia"),
                    ("AW", "Vincitore di giochi"),
                ],
                default="PP",
                max_length=2,
            ),
            preserve_default=False,
        ),
    ]
