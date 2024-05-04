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


def in_development(request):
    data = {

    }
    template_name = "main/in_development.html"
    return render(request, template_name, data)
