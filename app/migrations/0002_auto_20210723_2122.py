# Generated by Django 2.2.13 on 2021-07-24 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='eye_color',
            field=models.CharField(choices=[('BLACK', 'BLACK'), ('BROWN', 'BROWN'), ('YELLOW', 'YELLOW'), ('RED', 'RED'), ('GREEN', 'GREEN'), ('PURPLE', 'PURPLE'), ('UNKNOWN', 'UNKNOWN')], default='UNKNOWN', max_length=32),
        ),
        migrations.AlterField(
            model_name='people',
            name='hair_color',
            field=models.CharField(choices=[('BLACK', 'BLACK'), ('BROWN', 'BROWN'), ('BLONDE', 'BLONDE'), ('RED', 'RED'), ('WHITE', 'WHITE'), ('BALD', 'BALD')], default='BLACK', max_length=32),
        ),
    ]