from django.db import models


class voice_qamodel(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()


