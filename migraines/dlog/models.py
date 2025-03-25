from django.db import models

# Create your models here.

#2
class user_login(models.Model):
    user_email = models.EmailField(max_length=100, unique=True, blank=False)
    user_password = models.CharField(max_length=128)  # Field for storing the hashed password


    def __str__(self):
        return self.user_email        
    
#3
class migraines_log(models.Model):
    user_email = models.ForeignKey(user_login, on_delete=models.CASCADE)
    log_date = models.DateField()

    def __str__(self):
        return f"{self.user_email} {self.log_date}"
    
    class Meta:
        ordering = ["log_date"]