# Generated by Django 2.1.2 on 2018-11-02 15:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='session_expire',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='session_key',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
