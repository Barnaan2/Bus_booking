# Generated by Django 4.1.2 on 2022-10-12 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='busseat',
            name='seat_number',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
    ]
