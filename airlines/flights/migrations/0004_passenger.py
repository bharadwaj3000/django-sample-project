# Generated by Django 3.2.6 on 2021-12-22 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_delete_passengers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('flights', models.ManyToManyField(blank=True, related_name='passengers', to='flights.Flight')),
            ],
        ),
    ]
