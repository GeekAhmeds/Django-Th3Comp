# Generated by Django 3.2.9 on 2021-12-25 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('desc', models.TextField()),
                ('image', models.ImageField(upload_to=None)),
            ],
            options={
                'verbose_name': 'AboutUs',
                'verbose_name_plural': 'AboutUss',
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=250)),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name': 'ContactUs',
                'verbose_name_plural': 'ContactUss',
            },
        ),
    ]
