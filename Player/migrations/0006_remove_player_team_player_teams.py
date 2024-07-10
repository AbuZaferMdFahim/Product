# Generated by Django 5.0.7 on 2024-07-10 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Player', '0005_alter_player_team'),
        ('Team', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='team',
        ),
        migrations.AddField(
            model_name='player',
            name='teams',
            field=models.ManyToManyField(blank=True, related_name='players', to='Team.team'),
        ),
    ]