from django.db import models
# from django.contrib.auth.models import User

# class Member(models.Model):
#     name = models.CharField(max_length=55)
#     author = models.ForeignKey(User)
#     body = models.TextField()
#
#     def __str__(self):
#         return '{}{}'.format(self.title, self.author)


# class Account(m)

class Appointments(models.Model):
    # date = models.DateTimeField()
    title = models.CharField(max_length=10)
    note = models.TextField(blank=True, null=True)
    slug = models.SlugField()
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return '{} - {}'.format(self.title, self.date)