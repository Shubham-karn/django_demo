# Generated by Django 4.2.2 on 2023-07-20 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_renter',
        ),
        migrations.AddField(
            model_name='user',
            name='isRenter',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='occupation',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='profilePicture',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
