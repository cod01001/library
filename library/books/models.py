from django.db import models

class Category (models.Model):
    name_category = models.CharField(max_length=25)
    def __str__(self):
        # Возвращаем имя проекта в качестве его name
        return self.name_category

class Author (models.Model):
    name_author = models.CharField(max_length=25)
    def __str__(self):
        # Возвращаем имя проекта в качестве его name
        return self.name_author

class Books (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.FileField(upload_to="img/")
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='category')
    author = models.ManyToManyField('Author', related_name='author')
    def __str__(self):
        # Возвращаем имя проекта в качестве его title
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=25)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Books', on_delete=models.CASCADE)
    def __str__(self):
        # Возвращаем имя проекта в качестве его title
        return self.title