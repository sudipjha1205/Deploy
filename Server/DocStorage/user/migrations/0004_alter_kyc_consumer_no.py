# Generated by Django 4.2.8 on 2023-12-22 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_kyc_consumer_no_alter_kyc_pdf_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kyc',
            name='consumer_no',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]