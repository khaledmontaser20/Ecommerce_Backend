# Generated by Django 3.2.7 on 2021-12-15 08:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='img',
            field=models.ImageField(default=2, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
