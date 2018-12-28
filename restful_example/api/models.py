from django.db import models

# Create your models here.
class User(models.Model):
    TYPE_CHOICES =(
        (1,'LV1'),
        (2,'LV2'),
        (3,'LV3'),
        (4,'LV4'),
        (5,'LV5'),
        (6,'LV6')
    )
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    user_type = models.SmallIntegerField(choices=TYPE_CHOICES,default=1)

    def __str__(self):
        return self.name


class Token(models.Model):
    user = models.ForeignKey(to='User',on_delete=models.CASCADE)
    token = models.CharField(max_length=128)

    def __str__(self):
        return self.token


class Movie(models.Model):
    name = models.CharField(verbose_name="片名",max_length=32)
    poster = models.ImageField(upload_to="./imgs",verbose_name='海报')
    movie_detail = models.OneToOneField(to='MovieDetail',on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# 电影详情
class MovieDetail(models.Model):
    LANGUAGE_CHOICES =(
        (1,'汉语普通话'),
        (2,'英语'),
        (3,'日语'),
        (4,'韩语'),
        (5,'法语'),
        (6,'俄语'),
        (7,'西班牙语'),
        (8,'阿拉伯语'),
        (9,'其他语言'),
    )
    CAPTIONS_CHOICES =(
        (1,'中文字幕'),
        (2,'英文字幕'),
    )
    name = models.CharField(verbose_name="片名",max_length=32)
    date = models.IntegerField(verbose_name="年代")
    language = models.SmallIntegerField(verbose_name='语言',choices=LANGUAGE_CHOICES,default=1)
    category = models.ForeignKey(verbose_name='类别',to='Category',on_delete=models.CASCADE)
    captions = models.SmallIntegerField(verbose_name='字幕',choices=CAPTIONS_CHOICES,default=1)
    durations = models.SmallIntegerField(verbose_name="时长")
    directors = models.ManyToManyField(verbose_name='导演',to='Person',
                                       related_name='direct',related_query_name='direct')
    screenwriter = models.ManyToManyField(verbose_name="编剧",to='Person',
                                          related_name='writer',related_query_name='writer')
    actors = models.ManyToManyField(verbose_name='演员',to='Person',
                                        related_name='play',related_query_name='play')
    descriptions = models.CharField(verbose_name='简介',max_length=512)

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Category(models.Model):
    title =models.CharField(max_length=16)

    def __str__(self):
        return self.title
