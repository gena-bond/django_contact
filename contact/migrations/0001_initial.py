# Generated by Django 4.0 on 2021-12-24 09:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('middle_name', models.CharField(max_length=100, verbose_name='Отчество')),
                ('mobile_phone', models.CharField(max_length=20, verbose_name='Мобильный телефон')),
                ('work_phone', models.CharField(max_length=20, verbose_name='Рабочий телефон')),
                ('organization', models.CharField(max_length=100, verbose_name='Организация')),
                ('e_mail', models.EmailField(max_length=254)),
                ('create_data', models.DateField(default=datetime.date.today, verbose_name='Дата создания')),
                ('edit_data', models.DateField(default=datetime.date.today, verbose_name='Дата редактирования')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
    ]
