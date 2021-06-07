from django.db import models

class Data(models.Model):
    api_key = models.CharField(max_length = 100)
    api_secreat_key = models.CharField(max_length = 100)
    access_token = models.CharField(max_length = 100)
    access_token_secreat = models.CharField(max_length = 100)
    hashtag = models.CharField(max_length = 100)
    numbers = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return self.comment

