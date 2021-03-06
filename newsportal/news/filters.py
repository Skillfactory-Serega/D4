from django_filters import FilterSet
from .models import Post

# Создаем свой набор фильтров для модели Post.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class PostFilter(FilterSet):
   class Meta:
       # В Meta классе мы должны указать Django модель,
       # в которой будем фильтровать записи.
       model = Post
       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
       fields = {
           # поиск по автору
           'author' : ['exact'],
            #поиск по названию
           'title': ['exact'],
           # поиск по дате
           'dateCreation' : ['gte'],
           # поиск по категории
           #'postCategory' : ['exact']
       }