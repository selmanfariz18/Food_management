# Generated by Django 4.2.1 on 2023-11-07 16:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0005_quote"),
    ]

    operations = [
        migrations.AddField(
            model_name="food",
            name="taken_by",
            field=models.CharField(max_length=20, null=True),
        ),
    ]