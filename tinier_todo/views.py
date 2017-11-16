from django.shortcuts import render
from django.utils import timezone

from .models import Item


def latest_posts(request):
    items = Item.objects.filter(date_created=timezone.now()).order_by('date_created')
    return render(request, 'todo_list.html', {'items': items})


def home_page(request):
    return render(request, 'main.html')


def add_item(request):
    if  request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']

        todo = Item(title=title, text=text)
        todo.save()

        return render(request, 'add.html')
    else:
        return render(request, 'main.html')