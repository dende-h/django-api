from django.db import models

# Create your models here.
# 以下を追加
class WorldSetting(models.Model):

    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
