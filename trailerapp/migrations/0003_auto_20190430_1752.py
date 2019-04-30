# Generated by Django 2.1.7 on 2019-04-30 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trailerapp', '0002_auto_20190430_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='door',
            name='status',
            field=models.CharField(choices=[('Empty', 'Empty'), ('Loaded', 'Loaded'), ('In Progress', 'In Progress'), ('None', 'None')], default='3', max_length=20),
        ),
    ]
