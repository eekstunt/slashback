# Generated by Django 2.1 on 2019-03-15 10:07

import cashback_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashback_app', '0089_auto_20190314_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='earned',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Заработано, RUB'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=cashback_app.models.Photo(blank=True, null=True, upload_to=cashback_app.models.Photo.get_path, validators=[cashback_app.models.Photo.validate_image], verbose_name='Изображение, до 5МБ'),
        ),
        migrations.AlterField(
            model_name='texts',
            name='referral_invite_telegram_button',
            field=models.CharField(default='-', max_length=256, verbose_name='Кнопка запуска бота'),
        ),
        migrations.AlterField(
            model_name='texts',
            name='referral_invite_telegram_message',
            field=models.TextField(default='-', verbose_name='Текст приглашения в Telegram'),
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
