# Generated by Django 4.2.7 on 2023-11-13 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("WhatsafPortal", "0012_remove_feature_beta_feature_stable"),
    ]

    operations = [
        migrations.AlterField(
            model_name="feature",
            name="Image",
            field=models.ImageField(upload_to="FeaturesPhoto"),
        ),
    ]
