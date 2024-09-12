from django.shortcuts import render
import requests
from .forms import PublicUrlForms


def get_disk(public_key):
    """Получение списка файлов/папок с помощью публичной ссылки"""
    url = (f'https://cloud-api.yandex.net/v1/disk/public/resources?public_key={public_key}')
    response = requests.get(url=url)
    if response.status_code == 200:
        return response.json()


def index(request):
    """Отображения списка файлов/папок на странице"""
    form = PublicUrlForms(request.POST)
    if request.method == 'POST'and form.is_valid():
        public_key = form.cleaned_data['public_key']
        files = get_disk(public_key)
        content = files["_embedded"]["items"]
    context = {
        "content": content,
        "form": form
    }
    return render (request, "index.html", context)
