# Generated by Django 3.2.16 on 2023-01-28 23:58

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_id', models.UUIDField(auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('shop_name', models.CharField(max_length=255)),
                ('contact_address', models.TextField(max_length=1000)),
                ('postal_code', models.CharField(max_length=10)),
                ('business_type', models.CharField(choices=[('individual', 'Individual'), ('business entity', 'Business Entity'), ('company', 'Company')], max_length=20)),
                ('full_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=20)),
                ('extra_phone_number', models.CharField(max_length=20)),
                ('legal_id', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('referrer', models.EmailField(max_length=50)),
                ('no_of_employees', models.CharField(choices=[('1-20', '1 to 20'), ('20-50', '20 to 50'), ('50-100', '50 to 100'), ('above 100', 'above 100')], max_length=20)),
                ('business_reg_number', models.CharField(max_length=255, null=True)),
                ('registeration_certificate', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('legal_entity_country', models.CharField(max_length=255)),
                ('shipping_country', models.CharField(max_length=255)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='businesses', to='accounts.customer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
