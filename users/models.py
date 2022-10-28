from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    GENDERS = (
        ('m', 'Мужчина'),
        ('f', 'Женщина'),
    )

    gender = models.CharField('Пол', max_length=1, choices=GENDERS, default='')
    birth_date = models.DateField('День рождения', default='2000-01-01')
    avatar = models.ImageField('Аватарка', upload_to='avatars/', blank=True, null=True, default='standart_avatar.png')


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

