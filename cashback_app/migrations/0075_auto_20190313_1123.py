# Generated by Django 2.1 on 2019-03-13 11:23

import cashback_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashback_app', '0074_auto_20190313_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='financial',
            name='percent_top',
            field=models.DecimalField(decimal_places=2, default=15, max_digits=5, verbose_name='Повышенный, %'),
        ),
        migrations.AlterField(
            model_name='financial',
            name='admin_percent',
            field=models.DecimalField(decimal_places=2, default=5, max_digits=5, verbose_name='Процент от привлечения админов'),
        ),
        migrations.AlterField(
            model_name='financial',
            name='percent',
            field=models.DecimalField(decimal_places=2, default=5, max_digits=5, verbose_name='Стандартный, %'),
        ),
        migrations.AlterField(
            model_name='financial',
            name='percent_btb',
            field=models.DecimalField(decimal_places=2, default=75, max_digits=5, verbose_name='Партнерский процент'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=cashback_app.models.Photo(blank=True, null=True, upload_to=cashback_app.models.Photo.get_path, validators=[cashback_app.models.Photo.validate_image], verbose_name='Изображение, до 5МБ'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='photo',
            field=cashback_app.models.Photo(upload_to=cashback_app.models.Photo.get_path, validators=[cashback_app.models.Photo.validate_image], verbose_name='Фото программы'),
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