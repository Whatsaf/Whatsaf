# Generated by Django 4.2.7 on 2023-12-24 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("WhatsafPortal", "0024_remove_userwhatsappdetail_userabout_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userwhatsappdetail",
            name="UserContact",
            field=models.CharField(choices=[["Contacts", "Contacts"]], max_length=500),
        ),
    ]
