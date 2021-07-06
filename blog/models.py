from django.db import models

class Article(models.Model):
    name      = models.CharField(max_length=255)
    summary   = models.CharField(max_length=255)
    content   = models.TextField()
    post_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-post_date',)

    def __str__(self):
        return self.name

class Comment(models.Model):
    article  = models.ForeignKey(Article, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    body     = models.TextField()
    post_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-post_date',)

    def __str__(self):
        return f"{self.username} on {self.post_date}"
