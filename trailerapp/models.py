from django.db import models


class Door(models.Model):
    door_number = models.IntegerField()
    trailer_number = models.CharField(max_length=100, default='No Trailer', blank=True)
    EMPTY = 'Empty'
    LOADED = 'Loaded'
    PROGRESS = 'In Progress'
    NONE = 'None'
    PUSHBACK = 'Pushback'
    STATUS_CHOICES = (
        (NONE, 'None'),
        (LOADED, 'Loaded'),
        (PROGRESS, 'In Progress'),
        (EMPTY, 'Empty'),
        (PUSHBACK, 'Pushback'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='3')

    def __str__(self):
        return str(self.door_number) + ' | ' + self.trailer_number + ' | ' + self.status
