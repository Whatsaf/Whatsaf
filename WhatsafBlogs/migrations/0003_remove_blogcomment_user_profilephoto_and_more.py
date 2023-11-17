# Generated by Django 4.2.7 on 2023-11-17 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("WhatsafBlogs", "0002_remove_blog_blogcategory_alter_blogcomment_date"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blogcomment",
            name="User_ProfilePhoto",
        ),
        migrations.AlterField(
            model_name="blog",
            name="BlogImage",
            field=models.ImageField(upload_to="BlogImages"),
        ),
        migrations.AlterField(
            model_name="blogcomment",
            name="ActualDate",
            field=models.CharField(default="17-11-2023", max_length=40),
        ),
        migrations.AlterField(
            model_name="blogcomment",
            name="Date",
            field=models.CharField(default="2023-11-17 20:16:40.773843", max_length=40),
        ),
    ]
