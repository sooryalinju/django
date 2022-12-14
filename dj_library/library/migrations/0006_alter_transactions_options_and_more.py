# Generated by Django 4.1 on 2022-09-04 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_alter_transactions_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transactions',
            options={},
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='status',
        ),
        migrations.AddField(
            model_name='books',
            name='availability',
            field=models.BooleanField(blank=True, null=True, verbose_name='Availability'),
        ),
        migrations.AddField(
            model_name='books',
            name='status',
            field=models.CharField(blank=True, choices=[('i', 'Issued'), ('r', 'Returned')], default='r', help_text='Staus', max_length=1),
        ),
    ]
