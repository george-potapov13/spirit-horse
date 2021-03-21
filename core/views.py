from django.shortcuts import render


VICTIMS = [
    'https://www.djangoproject.com/',
    'www.django-rest-framework.org',
    'https://pythonworld.ru/',
    'www.python.org'
]


def index(request):
    # data =
    template_name = 'core/index.html'
    context = {'data', data}
    return render(request, template_name, context)
