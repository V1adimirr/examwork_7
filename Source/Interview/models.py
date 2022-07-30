from django.db import models
from django.db.models import CASCADE


class Poll(models.Model):
    question = models.TextField(max_length=150, verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.id}. {self.question}: {self.created_at}"

    class Meta:
        db_table = "Poll"
        verbose_name = "Опрос"
        verbose_name_plural = "Опросы"


class Choice(models.Model):
    option = models.TextField(max_length=100, verbose_name='Вариант ответа')
    interview = models.ForeignKey('Interview.Poll', related_name='Poll', on_delete=CASCADE, verbose_name='Опрос')

    def __str__(self):
        return f"{self.id}. {self.option}: {self.interview}"

    class Meta:
        db_table = "Choice"
        verbose_name = "Вариант"
        verbose_name_plural = "Варианты"
