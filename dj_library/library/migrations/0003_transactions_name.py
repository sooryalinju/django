# Generated by Django 4.1 on 2022-09-03 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_members_transactions_ids_transactions_book_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Transaction No.'),
        ),
    ]