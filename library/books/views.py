from django.shortcuts import render
from .models import Books, Category
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
    # Post - занвание модели
    # .objects.get - достать только определенную запись
    # (pk=pk) персональный ключ по которому будет доставать из бд
    post = Books.objects.get(pk=pk)
    form = CommentForm()



    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=post
            )
            comment.save()

    # comments - переменная отправляеь запрос в бд и достает сообщения относящиеся к выбронаму посту
    comments = Comment.objects.filter(post=post)


    # создание словаря для дальнейшего вывода в HTML
    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }

    # указываем какой HTML файл будем вызывать
    return render(request, 'blog_detail.html', context)



def books_category(request,category):
    category = Category.name.filter(
        categories__name__contains=category
    ).order_by('-created_on')

    context = {
        'category': category,

    }
    return render(request,'books_category.html', context)








