from django.db import models

# Create your models here.
NULLABLE = {'null': True, 'blank': True}


class Student(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='имя')
    last_name = models.CharField(max_length=100, verbose_name='фамилия')
    avatar = models.ImageField(upload_to='students/', verbose_name='аватар', **NULLABLE)

    email = models.EmailField(max_length=150, verbose_name='email', unique=True, **NULLABLE)

    is_active = models.BooleanField(default=True, verbose_name='статус обучения')

    def __str__(self):
        return f'{self.first_name}  {self.last_name}'

    class Meta:
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'
        ordering = ('last_name', )
