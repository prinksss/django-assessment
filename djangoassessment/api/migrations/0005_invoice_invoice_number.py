# Generated by Django 4.2.5 on 2023-09-29 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_invoice_customer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='invoice_number',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
