from django.db import models

# Create your models here.
class Books (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.CharField(max_length=20)
    image = models.FileField(upload_to="img/")

    def __str__(self):
        # Возвращаем имя проекта в качестве его title
        return self.title
