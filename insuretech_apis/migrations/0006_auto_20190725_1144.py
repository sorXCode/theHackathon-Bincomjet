# Generated by Django 2.2.3 on 2019-07-25 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insuretech_apis', '0005_auto_20190725_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ainsuranceuserprofile',
            name='registrationdate',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='ainsuranceuserprofile',
            name='token',
            field=models.CharField(default='2ZLIDEQ6OOH4HOE1G1NZZQZED5KZK3B1HXKTF1MIA6D4XD9R', max_length=100),
        ),
    ]