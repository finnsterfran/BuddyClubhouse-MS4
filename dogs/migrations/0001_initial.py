# Generated by Django 3.2.8 on 2021-11-30 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('resided_since', models.DateField()),
                ('gender', models.CharField(choices=[('Female', 'female'), ('Male', 'male')], max_length=6)),
                ('image', models.ImageField(blank=True, null=True, upload_to='dogs/')),
                ('story', models.TextField(blank=True, max_length=2000)),
                ('breed', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dogs.breed')),
                ('job', models.ManyToManyField(blank=True, to='dogs.Job')),
            ],
            options={
                'ordering': ['resided_since'],
            },
        ),
    ]
