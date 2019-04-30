from django.db import models


class Door(models.Model):
    door_number = models.IntegerField()
    trailer_number = models.CharField(max_length=100, default='No Trailer')
    EMPTY = 'Empty'
    LOADED = 'Loaded'
    PROGRESS = 'In Progress'
    NONE = 'None'
    STATUS_CHOICES = (
        (NONE, 'None'),
        (LOADED, 'Loaded'),
        (PROGRESS, 'In Progress'),
        (EMPTY, 'Empty'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='3')

    def __str__(self):
        return self.door_number + ' | ' + self.trailer_number + ' | ' + self.status
