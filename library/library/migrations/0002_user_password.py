# Generated by Django 2.1.2 on 2018-11-02 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
