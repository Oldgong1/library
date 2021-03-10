from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Speaker(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    date_of_birth = models.DateField(null=True, blank=True)
    Bio = models.TextField(max_length=350, null=True, blank=True, help_text='Enter speaker biography')


    def __str__(self):
        return f'{self.last_name}, {self.date_of_birth}' 

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('speaker-detail', args=[str(self.id)])


class Speech(models.Model):
    title = models.CharField(max_length=128)
    date = models.DateTimeField()
    speaker = models.ForeignKey(Speaker, on_delete=models.PROTECT)
    body = models.TextField()
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"        
           