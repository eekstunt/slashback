# Generated by Django 2.1 on 2019-02-26 16:05

import cashback_app.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cashback_app', '0027_auto_20190226_1555'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_name',
            new_name='name',
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
