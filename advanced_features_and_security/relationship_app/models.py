from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=['Admin', 'Librarian', 'Memeber'])


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        userprofile.objects.create(user=instance)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()

    class Meta:
        permissions = (
            ('is admin', 'Is Admin'),
            ('can_add_book', 'Can Add Book'),
            ('can_delete_book', 'Can Delete Book'),
            ('can_change_book', 'Can Change Book'),
        )
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=[('Admin', 'Admin'), ('Librarian', 'Librarian'), ('Member', 'Member')])





