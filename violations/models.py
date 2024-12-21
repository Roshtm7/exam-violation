from django.db import models
from django.contrib.auth.models import User



class Violation(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE)

    description=models.TextField()

    image=models.ImageField(upload_to='Violations/')

    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.user
