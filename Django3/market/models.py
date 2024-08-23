from django.db import models



class LastNews(models.Model):
  title = models.TextField()
  time = models.CharField(max_length=255)
