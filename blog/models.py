from django.db import models


# Create your models here.
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Author(TimeStampedModel):
    name = models.CharField(max_length=212)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    profession = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class Tag(TimeStampedModel):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class Post(TimeStampedModel):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=212)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)
    second_title = models.CharField(max_length=212)
    second_content = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class Comment(TimeStampedModel):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=212)
    website = models.URLField()
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


class About(TimeStampedModel):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    name = models.CharField(max_length=212)
    body = models.TextField()

    def __str__(self):
        return self.name
