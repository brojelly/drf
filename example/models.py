from django.db import models

class Book(models.Model):
    bid = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    pages = models.IntegerField()
    price = models.IntegerField()
    published_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title #어드민 페이지에서 ...OBJECT(1) 요딴식으로 안나옴