# Generated by Django 4.2.5 on 2023-09-14 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_image',
            field=models.ImageField(default='default.jpg', upload_to='book_images'),
        ),
    ]
