from django.db import models


class ResponseCode(models.Model):
    url = models.URLField(max_length=200)
    code = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url
