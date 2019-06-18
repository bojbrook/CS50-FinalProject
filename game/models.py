from django.db import models

# Create your models here.
class studio(models.Model):
    name = models.CharField(max_length=64, primary_key=True)

    def __str__(self):
        return f"{self.name}"

class game(models.Model):
    title = models.CharField(max_length=64)
    studio = models.ForeignKey(studio, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - by {self.studio}"