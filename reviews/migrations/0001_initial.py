# Generated by Django 4.2.1 on 2023-05-12 11:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('context', models.TextField(max_length=255)),
                ('stars', models.PositiveIntegerField(choices=[(1, '1점'), (2, '2점'), (3, '3점'), (4, '4점'), (5, '5점')], default=0)),
                ('point', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('booked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booked_users', to='hotels.book')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_set', to='hotels.rooms')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
