from django.db import models


# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=True)
    hcomment = models.CharField(max_length=100)
    hbook = models.ForeignKey("BookInfo")
