# Generated by Django 2.1 on 2019-02-28 12:03

import cashback_app.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashback_app', '0043_auto_20190228_1119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания, UTC')),
                ('status', models.CharField(choices=[('created', 'Создан'), ('postponed', 'Отложен'), ('queue', 'В очереди'), ('process', 'Рассылается'), ('done', 'Разослан')], default='created', max_length=9, verbose_name='Статус')),
                ('photo', cashback_app.models.Photo(blank=True, null=True, upload_to=cashback_app.models.Photo.get_path, validators=[cashback_app.models.Photo.validate_image], verbose_name='Изображение, до 5МБ')),
                ('message', models.TextField(max_length=1024, verbose_name='Форматированный текст, до 1024 символов')),
                ('button_text', models.CharField(blank=True, max_length=50, null=True, verbose_name='Текст кнопки')),
                ('button_url', models.URLField(blank=True, null=True, verbose_name='Ссылка кнопки')),
                ('postpone', models.BooleanField(default=False, verbose_name='Отложить')),
                ('postpone_time', models.DateTimeField(default=datetime.datetime(2020, 1, 1, 0, 0), verbose_name='Время публикации, UTC')),
                ('amount_of_receivers', models.IntegerField(blank=True, null=True, verbose_name='Количество получателей')),
            ],
            options={
                'verbose_name': 'пост',
                'verbose_name_plural': 'посты',
            },
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
