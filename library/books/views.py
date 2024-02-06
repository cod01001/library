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
    books = Books.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=books
            )
            comment.save()

    # comments - переменная отправляеь запрос в бд и достает сообщения относящиеся к выбронаму посту
    comments = Comment.objects.filter(post=books)

    # создание словаря для дальнейшего вывода в HTML
    context = {
        'books': books,
        'comments': comments,
        'form': form,
    }

    # указываем какой HTML файл будем вызывать
    return render(request, 'books_detail.html', context)



def books_category(request,category):
    category = Category.objects.filter(
        categories__name__contains=category
    ).order_by('-created_on')

    context = {
        'category': category,

    }
    return render(request,'books_category.html', context)


# print(1)





