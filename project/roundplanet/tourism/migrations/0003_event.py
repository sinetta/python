# Generated by Django 3.2.12 on 2023-12-28 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0002_package'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img')),
                ('description', models.CharField(max_length=255)),
            ],
        ),
    ]