# Generated by Django 4.2.7 on 2023-12-24 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("WhatsafPortal", "0028_userwhatsappdetail_userabout_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="userwhatsappdetail",
            name="UserName",
            field=models.CharField(default="", max_length=500),
        ),
    ]
