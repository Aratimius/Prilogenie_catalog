# Generated by Django 5.1.1 on 2024-09-24 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_alter_blog_preview"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="preview",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="blog/photo",
                verbose_name="изображение",
            ),
        ),
    ]
