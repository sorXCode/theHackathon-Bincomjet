# Generated by Django 2.2.3 on 2019-07-25 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insuretech_apis', '0006_auto_20190725_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ainsuranceuserprofile',
            name='token',
            field=models.CharField(default='1R51OZYZX0DJBZZ52L9UY3LHURBZP8SQXFDDSI6HM5HGURCJ', max_length=100),
        ),
    ]
