# Generated by Django 3.2.8 on 2021-11-27 21:09

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('dogs', '0002_alter_dog_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('date_of_entry', models.DateTimeField(auto_now_add=True)),
                ('featured_image', models.ImageField(blank=True, null=True, upload_to='blogs/')),
                ('blog_entry', models.TextField(blank=True, max_length=3000, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name_of_buddy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dogs.dog')),
                ('username', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]