from django.db import models

class Author (models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name

class Publisher(models.Model):
    title = models.TextField()
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.title

class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    copy_count = models.SmallIntegerField(default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



