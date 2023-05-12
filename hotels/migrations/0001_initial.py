<<<<<<< HEAD
# Generated by Django 4.2.1 on 2023-05-12 01:02
=======
# Generated by Django 4.2.1 on 2023-05-11 10:59
>>>>>>> 427f681 (5월 12일 저녁 머지)

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import hotels.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Spots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, validators=[hotels.validators.contains_special_character])),
                ('call_number', models.CharField(max_length=100, validators=[hotels.validators.validate_phone_number])),
                ('location', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, validators=[hotels.validators.contains_special_character])),
                ('description', models.TextField(error_messages='10자 이상 입력하셔야합니다.', max_length=300, validators=[django.core.validators.MinLengthValidator(10)])),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('max_members', models.IntegerField()),
                ('status', models.CharField(choices=[('checkin', 'checkin'), ('empty', 'empty')], max_length=10)),
                ('spot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.spots')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('members', models.IntegerField(default=1)),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookset', to='hotels.rooms')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
