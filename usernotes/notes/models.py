from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    title = models.CharField(max_length=30)
    pub_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(null=False, blank=False)
    user = models.ForeignKey(User, related_name='notes', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} by {self.user.username}"
