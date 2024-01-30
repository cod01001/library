from django.db import models

class Category (models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        # Возвращаем имя проекта в качестве его name
        return self.name

class Books (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.CharField(max_length=25)
    image = models.FileField(upload_to="img/")
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    def __str__(self):
        # Возвращаем имя проекта в качестве его title
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    def __str__(self):
        # Возвращаем имя проекта в качестве его title
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=25)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    def __str__(self):
        # Возвращаем имя проекта в качестве его title
        return self.title