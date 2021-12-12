# Generated by Django 3.2.8 on 2021-12-12 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date_of_event', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('buddy_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dogs.dog')),
                ('event_type', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='events.event_type')),
            ],
        ),
    ]
