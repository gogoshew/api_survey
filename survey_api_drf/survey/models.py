from django.db import models
from django.contrib.auth.models import User


class Survey(models.Model):
    survey_name = models.CharField(max_length=200, verbose_name='Опрос')
    pub_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now=True)
    survey_description = models.CharField(max_length=200, verbose_name='Описание опроса')

    def __str__(self):
        return self.survey_name


class Question(models.Model):
    type_choices = (
        ('one', 'Один вариант'),
        ('multiple', 'Несколько вариантов'),
        ('text', 'Текстовый вариант'),
    )
    survey = models.ForeignKey(Survey, related_name='questions', verbose_name='Опрос', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200, verbose_name='Текст вопроса')
    question_type = models.CharField(max_length=200, verbose_name='Тип вопроса', choices=type_choices)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', verbose_name='Вопрос', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text


class Answer(models.Model):
    user = models.ForeignKey(User, related_name='user', verbose_name='Пользователь', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='question', verbose_name='Вопрос', on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, related_name='choice', verbose_name='Вариант ответа', on_delete=models.CASCADE, null=True)
    answer_text = models.CharField(max_length=200, verbose_name='Ответ', null=True)

    def __str__(self):
        return self.answer_text