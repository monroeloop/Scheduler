from django.db import models


class Appointment(models.Model):
    title = models.CharField(max_length=10)
    note = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return '{} - {} - {}'.format(self.title, self.start, self.end)