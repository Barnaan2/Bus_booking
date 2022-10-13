# Generated by Django 4.1.2 on 2022-10-12 18:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0001_initial'),
        ('booker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55, unique=True)),
                ('type', models.CharField(max_length=55)),
                ('shortcode', models.TextField(max_length=20)),
                ('company_logo', models.ImageField(default='payment_method.png', null=True, upload_to='')),
                ('description', models.TextField(max_length=200)),
                ('contact', models.TextField(max_length=20)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-created', '-updated'),
            },
        ),
        migrations.CreateModel(
            name='PaymentInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_holder_name', models.CharField(max_length=100)),
                ('account_number', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=20)),
                ('verified', models.BooleanField(default=False, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('payment_method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.paymentmethod')),
                ('subroute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booker.subroute')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created', '-updated'),
            },
        ),
        migrations.CreateModel(
            name='FinishPayment',
            fields=[
                ('booking', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='finishpymnt_booking', serialize=False, to='booking.booking')),
                ('full_name', models.CharField(max_length=60)),
                ('transaction_id', models.CharField(max_length=255, null=True)),
                ('picture', models.ImageField(default='payment_method.png', null=True, upload_to='')),
                ('amount', models.FloatField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('payment_information', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.paymentinformation')),
            ],
            options={
                'unique_together': {('booking', 'transaction_id')},
            },
        ),
    ]
