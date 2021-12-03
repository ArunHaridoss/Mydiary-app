from django.db import models

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=50)
    notes = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Notes"
        ordering =['-created','-updated']

    def __str__(self):
        return self.title
