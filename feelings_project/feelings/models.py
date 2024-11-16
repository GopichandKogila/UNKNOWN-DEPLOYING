from django.db import models

class Feeling(models.Model):
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]

class Comment(models.Model):
    feeling = models.ForeignKey(Feeling, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment on {self.feeling.text[:20]} by Anonymous"
