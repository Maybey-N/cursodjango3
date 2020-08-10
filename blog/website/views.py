from django.shortcuts import render
from .models import Post

# Create your views here.
def hello_blog(request):
    lista = ['Django', 'Python', 'Git', 'Html',
             'Banco de dados', 'Linux', 'Nginx', 'Uwsgi',
              'Systemctl'
    ]
    list_post = Post.objects.all()

    data = {
        'name': 'Curso Django 3',
        'lista_tecnologia': lista,
        'posts': list_post,
    }

    return render(request, 'index.html', data)