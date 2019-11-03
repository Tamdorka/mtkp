from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model
from django.db import models
from phone_field import PhoneField

# Create your models here.

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class Lesson(models.Model):
    name = models.CharField(
        verbose_name = 'Название пары',
        default = '',
        max_length = 50
    )
    
    class Meta:
        verbose_name = 'Пара'
        verbose_name_plural = 'Пары'

class LessonDayLink(models.Model):
    day = models.PositiveSmallIntegerField(
        default = 1,
        verbose_name = 'Номер дня недели'
    )
    lesson = models.OneToOneField(
        to = Lesson,
        null = True,
        verbose_name = 'Пара',
        on_delete = models.CASCADE
    )
    number = models.PositiveSmallIntegerField(
        default = 1,
        verbose_name = 'Порядковый номер пары'
    )
    room = models.PositiveSmallIntegerField(
        default = 1,
        verbose_name = 'Кабинет'
    )
    group = models.ForeignKey(
        null = True,
        verbose_name = 'Группа',
        to = Group,
        on_delete = models.CASCADE
    )
    is_change = models.BooleanField(
        default = False,
        verbose_name = 'Замена'
    )
    week = models.PositiveSmallIntegerField(
        default = 0,
        verbose_name = 'Неделя'
    )
    
    class Meta:
        verbose_name = 'Ссылка пара-день'
        verbose_name_plural = 'Ссылки пара-день'


class Code(models.Model):
    activated = models.BooleanField(default = False)
    code = models.CharField(
        default = '',
        max_length = 15,
        verbose_name = 'Код'
    )
    group = models.ForeignKey(
        null = True,
        verbose_name = 'Группа пользователя',
        to = Group,
        on_delete = models.CASCADE,
    )

class Student(models.Model):
    user = models.OneToOneField(
        to = User,
        null = True,
        verbose_name = 'Ядро пользователя',
        on_delete = models.CASCADE
    )
    phone = PhoneField(
        blank = True,
        verbose_name = 'Номер телефона',
        help_text = 'Контактный номер телефона',
    )
    birthday = models.DateField(
        null = True,
        verbose_name = 'День рождения студента'
    )
    enter_date = models.DateField(
        null = True,
        verbose_name = 'Дата поступления студента'
    )
    year = models.PositiveSmallIntegerField(
        default = 1,
        verbose_name = 'Курс обучения'
    )
    code = models.OneToOneField(
        to = Code,
        null = True,
        verbose_name = 'Личный код доступа',
        on_delete = models.CASCADE
    )
    id_link = models.CharField(
        default = '',
        max_length = 20,
        verbose_name = 'Ссылка на пользователя',
    )
    status = models.CharField(
        null = True,
        max_length = 25,
        verbose_name = 'Статус'
    )
    
    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

class Teacher(models.Model):
    user = models.OneToOneField(
        null = True,
        verbose_name = 'Ядро пользователя',
        to = User,
        on_delete = models.CASCADE
    )
    phone = PhoneField(
        blank = True,
        verbose_name = 'Номер телефона',
        help_text = 'Контактный номер телефона',
    )
    birthday = models.DateField(
        null = True,
        verbose_name = 'День рождения студента'
    )
    code = models.OneToOneField(
        to = Code,
        null = True,
        verbose_name = 'Личный код доступа',
        on_delete = models.CASCADE
    )
    id_link = models.CharField(
        default = '',
        max_length = 20,
        verbose_name = 'Ссылка на пользователя',
    )
    status = models.CharField(
        null = True,
        max_length = 25,
        verbose_name = 'Статус'
    )
    
    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


class Wallet(models.Model):
    user = models.OneToOneField(
        null = True,
        verbose_name = 'Ядро пользователя',
        to = User,
        on_delete = models.CASCADE
    )
    amount = models.PositiveSmallIntegerField(
        default = 0,
        verbose_name = 'Баланс'
    )
    is_valid = models.BooleanField(
        default = True,
        verbose_name = 'Действительный'
    )
    
    class Meta:
        verbose_name = 'Кошелёк'
        verbose_name_plural = 'Кошельки'

class Social(models.Model):
    user = models.ForeignKey(
        null = True,
        verbose_name = 'Ядро пользователя',
        to = User,
        on_delete = models.CASCADE
    )
    type = models.CharField(
        default = '',
        max_length = 10
    )
    link = models.CharField(
        default = '',
        max_length = 50
    )
    
    class Meta:
        verbose_name = 'Ссылка на соцсеть'
        verbose_name_plural = 'Ссылки на соцсети'