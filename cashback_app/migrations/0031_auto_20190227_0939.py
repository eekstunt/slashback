# Generated by Django 2.1 on 2019-02-27 09:39

import cashback_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashback_app', '0030_auto_20190226_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_referral_id',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='second_referral_id',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='texts',
            name='start_photo_0',
            field=cashback_app.models.Photo(blank=True, null=True, upload_to=cashback_app.models.Photo.get_path, validators=[cashback_app.models.Photo.validate_image], verbose_name='Фото #1'),
        ),
        migrations.AlterField(
            model_name='texts',
            name='start_photo_1',
            field=cashback_app.models.Photo(blank=True, null=True, upload_to=cashback_app.models.Photo.get_path, validators=[cashback_app.models.Photo.validate_image], verbose_name='Фото #2'),
        ),
        migrations.AlterField(
            model_name='texts',
            name='start_photo_2',
            field=cashback_app.models.Photo(blank=True, null=True, upload_to=cashback_app.models.Photo.get_path, validators=[cashback_app.models.Photo.validate_image], verbose_name='Фото #3'),
        ),
        migrations.AlterField(
            model_name='texts',
            name='start_photo_3',
            field=cashback_app.models.Photo(blank=True, null=True, upload_to=cashback_app.models.Photo.get_path, validators=[cashback_app.models.Photo.validate_image], verbose_name='Фото #4'),
        ),
    ]
