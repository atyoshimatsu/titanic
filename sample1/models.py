from django.db import models

class Passenger(models.Model):
    SEX_CHOICES = (
        ('male or female', '-'),
        ('male', 'M'),
        ('female','F')
    )

    PORT_CHOICES = (
        ('C', 'Cherbourg'),
        ('Q', 'Queenstown'),
        ('S', 'Southampton'),
    )

    name = models.CharField(max_length=100, blank=True, null=True)
    sex = models.CharField(max_length=6, choices=SEX_CHOICES, blank=True, null=True)
    survived = models.BooleanField()
    age = models.PositiveIntegerField(blank=True, null=True)
    ticket_class = models.PositiveSmallIntegerField(null=True)
    embarked = models.CharField(max_length=1, choices=PORT_CHOICES)

    def __str__(self):
        return self.name