# Generated by Django 4.1 on 2022-09-03 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_transactions_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactions',
            name='returned',
        ),
        migrations.AddField(
            model_name='transactions',
            name='status',
            field=models.CharField(blank=True, choices=[('l', 'Loaned'), ('r', 'Returned')], default='l', help_text='Transaction Staus', max_length=1),
        ),
    ]
