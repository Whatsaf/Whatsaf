# Generated by Django 4.2.7 on 2023-11-19 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("WhatsafPortal", "0020_userdetail_active_userdetail_browserid"),
    ]

    operations = [
        migrations.AddField(
            model_name="feature",
            name="Short",
            field=models.CharField(default="", max_length=1000),
        ),
    ]
