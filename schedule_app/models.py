from django.db import models

class TimeSlot(models.Model):
    day_of_week = models.CharField(max_length=10)
    start_time = models.TimeField()
    stop_time = models.TimeField()
    ids = models.JSONField()  # Can store a list of IDs
    camera_ids = models.JSONField()  # Can store a list of camera Ids

    def __str__(self):
        return f'{self.day_of_week}: {self.start_time} - {self.stop_time}'

