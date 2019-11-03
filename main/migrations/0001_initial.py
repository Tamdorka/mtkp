# Generated by Django 2.2.4 on 2019-10-27 08:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, verbose_name='Название пары')),
            ],
            options={
                'verbose_name': 'Пара',
                'verbose_name_plural': 'Пары',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Ядро пользователя')),
            ],
            options={
                'verbose_name': 'Преподаватель',
                'verbose_name_plural': 'Преподаватели',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', phone_field.models.PhoneField(blank=True, help_text='Контактный номер телефона', max_length=31, verbose_name='Номер телефона')),
                ('birthday', models.DateField(null=True, verbose_name='День рождения пользователя')),
                ('year', models.PositiveSmallIntegerField(default=1, verbose_name='Курс обучения')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Ядро пользователя')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенты',
            },
        ),
        migrations.CreateModel(
            name='LessonDayLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.PositiveSmallIntegerField(default=1, verbose_name='Номер дня недели')),
                ('number', models.PositiveSmallIntegerField(default=1, verbose_name='Порядковый номер пары')),
                ('room', models.PositiveSmallIntegerField(default=1, verbose_name='Кабинет')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.Group', verbose_name='Группа')),
                ('lesson', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Lesson', verbose_name='Пара')),
            ],
            options={
                'verbose_name': 'Ссылка пара-день',
                'verbose_name_plural': 'Ссылки пара-день',
            },
        ),
    ]
