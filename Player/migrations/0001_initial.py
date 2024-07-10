# Generated by Django 5.0.7 on 2024-07-10 07:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bio', models.TextField(null=True)),
                ('kit', models.IntegerField(unique=True)),
                ('position', models.CharField(choices=[('goalkeeper', 'Goalkeeper'), ('defender', 'Defender'), ('midfielder', 'Midfielder'), ('forward', 'Forward')], default='midfielder', max_length=50)),
                ('age', models.IntegerField()),
                ('img', models.ImageField(upload_to='player_images/')),
                ('NID_number', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=100, null=True)),
                ('nationality_image', models.ImageField(null=True, upload_to='player_nationality_images/')),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
