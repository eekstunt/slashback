# Generated by Django 2.1 on 2019-02-28 19:19

import cashback_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashback_app', '0045_auto_20190228_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='texts',
            name='message_ad',
            field=models.TextField(default='-', max_length=256, verbose_name='Сообщение'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=cashback_app.models.Photo(blank=True, null=True, upload_to=cashback_app.models.Photo.get_path, validators=[cashback_app.models.Photo.validate_image], verbose_name='Изображение, до 5МБ'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='photo',
            field=cashback_app.models.Photo(blank=True, null=True, upload_to=cashback_app.models.Photo.get_path, validators=[cashback_app.models.Photo.validate_image], verbose_name='Фото программы'),
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
