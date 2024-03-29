from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Note(models.Model):
    user = models.ForeignKey(User, related_name='notes', on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('notes:detail', kwargs={'pk':self.pk})
