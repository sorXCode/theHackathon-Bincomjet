# Generated by Django 2.2.3 on 2019-07-25 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insuretech_apis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ainsuranceuserprofile',
            name='token',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
