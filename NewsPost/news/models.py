from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from embed_video.fields import EmbedVideoField

new = 'NW'
confirmed = 'CF'
deleted = 'DL'

TYPE = [
    (new, 'новый отклик'),
    (confirmed, 'подтвержден'),
    (deleted, 'удален'),
]


class User(AbstractUser):
    code = models.CharField(max_length=15, blank=True, null=True)


class Category(models.Model):
    category = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.category.title()


class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=10000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    time_creation = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', default=None,
                              blank=True, null=True, verbose_name='Фото')
    photo2 = models.ImageField(upload_to='photos2/%Y/%m/%d/', default=None,
                               blank=True, null=True, verbose_name='Фото 2')
    video = EmbedVideoField(default=None, blank=True, null=True, verbose_name='Видео')
    video2 = EmbedVideoField(default=None, blank=True, null=True, verbose_name='Видео 2')

    def preview(self):
        text_post = self.text
        len_text = len(text_post)
        if len_text >= 124:
            return f'{text_post[0:124]}...'
        else:
            return text_post[0:len_text]

    def __str__(self):
        return f'Заголовок:{self.title.title()} Текст:{self.text} Автор:{self.author.username}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class Responses(models.Model):
    new = 'NW'
    confirmed = 'CF'
    deleted = 'DL'

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=10000)
    status = models.CharField(max_length=2, choices=TYPE, )
    time_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Отклик:{self.text}. Автор:{self.author.username}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.post.id)])


class News(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=10000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    time_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Заголовок:{self.title.title()} Текст:{self.text}'

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])
