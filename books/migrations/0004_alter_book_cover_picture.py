# Generated by Django 4.1.5 on 2023-02-12 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_cover_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_picture',
            field=models.ImageField(default='mem2.png', upload_to=''),
        ),
    ]
