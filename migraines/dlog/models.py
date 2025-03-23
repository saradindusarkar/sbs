from django.db import models

class Dlog(models.Model):
    log_date = models.DateField(unique=True, auto_now_add=True)  # Ensure the date is unique across all entries
 #   log_date = models.DateField()  # Ensure the date is unique across all entries

    def __str__(self):
        return str(self.log_date)

    class Meta:
        ordering = ['log_date']