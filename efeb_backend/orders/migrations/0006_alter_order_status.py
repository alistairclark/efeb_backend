# Generated by Django 4.0.6 on 2022-07-27 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_order_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('SUCCESS', 'Success'), ('PENDING', 'Pending'), ('FAILED', 'Failed')], default='PENDING', max_length=7),
        ),
    ]
