# Generated by Django 4.1.4 on 2022-12-11 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_testimonials'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonials',
            name='image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
