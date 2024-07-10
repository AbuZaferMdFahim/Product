# Generated by Django 5.0.7 on 2024-07-10 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Player', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='position',
            field=models.CharField(choices=[('goalkeeper', 'Goalkeeper'), ('defender', 'Defender'), ('midfielder', 'Midfielder'), ('forward', 'Forward')], default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='player',
            name='rating',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=5),
        ),
    ]