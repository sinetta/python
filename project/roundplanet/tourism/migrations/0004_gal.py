# Generated by Django 3.2.12 on 2023-12-28 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0003_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=3000)),
            ],
        ),
    ]
