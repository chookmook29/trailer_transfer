# Generated by Django 2.1.7 on 2019-05-01 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trailerapp', '0005_auto_20190430_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='door',
            name='status',
            field=models.CharField(choices=[('None', 'None'), ('Loaded', 'Loaded'), ('In Progress', 'In Progress'), ('Empty', 'Empty'), ('Pushback', 'Pushback')], default='3', max_length=20),
        ),
    ]
