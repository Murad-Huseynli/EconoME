import os
from django.shortcuts import redirect, render
from .models import Deal
from .serializers import DealSerializer
import json

def dealsView(request):
  template_name = 'deals/main.html'

  data = {
      'API_DEALS': os.getenv('API') + '/deals',
  }
  return render(request, template_name, data)



def dealsDetailView(request, pk):
  if request.user.is_authenticated == False or request.user.group != 'business':
    return redirect('login-view')
  
  template_name = 'deals/detail.html'
  deal = Deal.objects.get(id=pk)

  if request.method == 'POST':
    
    return redirect('deals-view')

  data = {
        'deal':deal
  }
  return render(request, template_name, data)