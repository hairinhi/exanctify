from django.db import models

class Blog(models.Model):

    content = models.CharField(max_length=40000)
    posted_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-posted_date']

