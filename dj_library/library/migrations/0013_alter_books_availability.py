# Generated by Django 4.1 on 2022-09-07 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0012_alter_books_availability_alter_books_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='availability',
            field=models.BooleanField(default=True, null=True, verbose_name='Availability'),
        ),
    ]
