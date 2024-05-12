from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    status = models.IntegerField( default=1,
        choices=(
            (1, 'Yosh kitobxon'),
            (2, 'Tajribali kitobxon'),
            (3, 'Qadrdon kitobxon'),
            (4, 'Buyuk kitobxon')
        )
    )
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='media/user/', blank=True, null=True)

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=100)

    def str(self):
        return self.name


class Author(models.Model):
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/author/')
    bio = models.TextField()
    description = models.TextField()
    birthday = models.DateTimeField()
    dead_day = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.full_name


class Books(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/books/')
    page = models.IntegerField()
    year = models.DateField()
    publisher = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    paper_book = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    audio_book = models.BooleanField(default=False)
    audio_book_file = models.FileField(upload_to='media/audio_book/', blank=True, null=True)
    electron_book = models.BooleanField(default=False)
    electron_book_file = models.FileField(upload_to='media/electron_book/', blank=True, null=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mark = models.FloatField()
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}-{self.book.name}"


class Quotes(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return f"{self.book.name}-{self.body}"