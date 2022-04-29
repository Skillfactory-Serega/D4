from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum, DateTimeField
from django.urls import reverse


# Create your models here.
class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete= models.CASCADE)
    ratingAuthor = models.SmallIntegerField(default=0)

    def __str__(self):
        return str(self.authorUser)




    def update_rating(self):
        postRat = self.post_set.aggregate(postRating=Sum('rating'))
        pRat = 0
        pRat += postRat.get('postRating')

        commentRat = self.authorUser.comment.set.aggrigate(commentRating=Sum('rating'))
        cRat = 0
        cRat += commentRat.get('commentRating')

        self.ratingAuthor = pRat *3 +cRat
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return str(self.name)


class Post(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE,null=True, verbose_name = 'Автор')

    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_CHOICES = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья'),
    )
    categoryType = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=ARTICLE, verbose_name = 'Тип публикации')
    dateCreation = models.DateTimeField(null=True, blank=True, verbose_name = 'дата')
    #date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    postCategory = models.ManyToManyField('Category', through='PostCategory',blank=True, verbose_name='Категория')
    title = models.CharField(max_length=128, verbose_name = 'Заголовок')
    text = models.TextField(default=0, verbose_name = 'Текст')
    rating = models.SmallIntegerField(default=0, verbose_name = 'Рэйтинг')
    #images = models.ImageField(default=0, upload_to='images/', verbose_name = 'Изображение')
    #related_name = 'post'



    def __str__(self):
        return self.text

    def __str__(self):
        return '{}'.format(self.title)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[0 : 124] + '...'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class PostCategory(models.Model):
    postThrough = models.ForeignKey('Post', on_delete=models.CASCADE, verbose_name='Новость(Статья)')
    categotyThorugh = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return f'{self.postThrough} {self.categotyThorugh}'


class Comment(models.Model):
    commentPost = models.ForeignKey('Post', on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def __str__(self):
        return self.text




