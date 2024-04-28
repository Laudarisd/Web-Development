# Generated by Django 4.2.1 on 2023-05-13 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ml_in_geotech', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CsvData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csv_file', models.FileField(upload_to='csv_files/')),
                ('training_features', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
