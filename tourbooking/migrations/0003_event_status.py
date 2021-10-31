# Generated by Django 3.2.8 on 2021-10-31 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourbooking', '0002_event_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
    ]
