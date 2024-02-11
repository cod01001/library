from django.shortcuts import render
from .models import Books, Category, Comment
from .forms import CommentForm


def books_index(request):
    books = Books.objects.all().order_by('-created_on')
    context = {
        'books': books
    }
    return render(request, 'books_index.html', context)



def books_detail(request,pk):
    # post - переменная которая выводить полную информацию по определенному посту id которого
    # выбрал пользователь
    # Books - занвание модели
    # .objects.get - достать только определенную запись
    # (pk=pk) персональный ключ по которому будет доставать из бд
    book = Books.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=book
            )
            comment.save()

    # comments - переменная отправляеь запрос в бд и достает сообщения относящиеся к выбронаму посту
    comments = Comment.objects.filter(post=book)

    # создание словаря для дальнейшего вывода в HTML
    context = {
        'book': book,
        'comments': comments,
        'form': form,
    }

    # указываем какой HTML файл будем вызывать
    return render(request, 'books_detail.html', context)






# создать функцию которая возвращает список книг отсортированных по определенной категории
# принимаем категорию которую запросил пользователь и
# сравниваем её с книгами и присвоенными им категориями
# 'category' какая категория приходит и будет фильтроваться
def books_category(request,category):
    # category_book - достать из бд только те книги, которые
    # приписаны искомой категории 'category'

    # filter
    # Возвращает QuerySet содержащие объекты
    # соответствующие заданным параметрам
    category_book = Books.objects.filter(
        categories__name__contains=category
    ).order_by('-created_on')

    # создание словаря для присвоения значений для дальнейшего использования в HTML
    context = {
        'category': category_book,

    }
    return render(request,'books_category.html', context)








