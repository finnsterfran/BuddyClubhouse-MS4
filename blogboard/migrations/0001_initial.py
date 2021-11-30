# Generated by Django 3.2.8 on 2021-11-30 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dogs', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date_of_entry', models.DateTimeField(auto_now_add=True)),
                ('featured_image', models.ImageField(blank=True, null=True, upload_to='blogs/')),
                ('blog_entry', models.TextField(max_length=3000)),
                ('buddy_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dogs.dog')),
                ('username', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]
