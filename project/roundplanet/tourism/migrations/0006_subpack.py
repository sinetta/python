# Generated by Django 3.2.12 on 2024-01-05 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0005_delete_subpack'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subpack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=50)),
                ('day', models.CharField(max_length=20)),
                ('night', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=255)),
                ('destination1', models.CharField(max_length=20)),
                ('destination2', models.CharField(max_length=20)),
                ('destination3', models.CharField(max_length=20)),
                ('image1', models.ImageField(upload_to='uploads/')),
                ('image2', models.ImageField(upload_to='uploads/')),
                ('image3', models.ImageField(upload_to='uploads/')),
                ('pack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tourism.subpackage')),
            ],
        ),
    ]
