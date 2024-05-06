import os
from django.shortcuts import render
from .models import Deal
from .serializers import DealSerializer
import json

def dealsView(request):
    template_name = 'deals/main.html'

    data = {
      'API_DEALS': os.getenv('API') + '/deals',
    }
    return render(request, template_name, data)



