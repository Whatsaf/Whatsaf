# Generated by Django 4.2.7 on 2023-11-13 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("WhatsafPortal", "0005_faq"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="faq",
            name="Name",
        ),
    ]
