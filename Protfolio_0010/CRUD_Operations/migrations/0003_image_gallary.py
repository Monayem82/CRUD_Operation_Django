# Generated by Django 4.2.7 on 2023-12-26 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD_Operations', '0002_insertdatabase_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='image_gallary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=None, null=True, upload_to='image_gallaye/')),
            ],
        ),
    ]
