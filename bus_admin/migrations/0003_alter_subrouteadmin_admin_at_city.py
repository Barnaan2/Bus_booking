# Generated by Django 4.1.1 on 2022-10-06 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('system_admin', '0001_initial'),
        ('bus_admin', '0002_route_bus_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subrouteadmin',
            name='admin_at_city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='system_admin.city'),
        ),
    ]
