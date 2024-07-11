# Generated by Django 5.0.7 on 2024-07-11 04:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Team', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bio', models.TextField(null=True)),
                ('Role', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('img', models.ImageField(upload_to='player_images/')),
                ('NID_number', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=100, null=True)),
                ('nationality_image', models.ImageField(null=True, upload_to='player_nationality_images/')),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='manager', to='Team.team')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]