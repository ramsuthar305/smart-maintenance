# Generated by Django 2.2 on 2019-05-08 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini', '0006_auto_20190507_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrations',
            name='status',
            field=models.CharField(default='available', max_length=200),
        ),
    ]