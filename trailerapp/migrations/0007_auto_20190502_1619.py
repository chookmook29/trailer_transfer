# Generated by Django 2.1.7 on 2019-05-02 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trailerapp', '0006_auto_20190501_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='door',
            name='trailer_number',
            field=models.CharField(blank=True, default='No Trailer', max_length=100),
        ),
    ]
