import logging

logger = logging.getLogger(__name__)

from django.shortcuts import render, redirect


def main(request):

    template_name = "main/index.html"
    data = {
            'title': 'Home | Econome',
            'section_class': 'index'
    }
    return render(request, template_name, data)

def about_us(request):
    template_name = "main/about_us.html"
    data = {

    }
    return render(request, template_name, data)


def in_development(request):
    template_name = "main/in_development.html"
    data = {

    }
    return render(request, template_name, data)
