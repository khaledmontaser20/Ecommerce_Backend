# Generated by Django 3.2.7 on 2021-12-15 08:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20211215_1041'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('review', models.TextField()),
                ('stars', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('features', models.TextField()),
                ('img', models.ImageField(upload_to='')),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('dimentions', models.IntegerField()),
                ('color', models.CharField(max_length=150)),
                ('materials', models.CharField(max_length=150)),
                ('size', models.CharField(max_length=150)),
                ('date', models.DateTimeField()),
                ('categories', models.ManyToManyField(to='data.Category')),
            ],
        ),
    ]