import os
from django.shortcuts import redirect, render
from .models import Deal
from .serializers import DealSerializer
import json
from django.conf import settings
import datetime
import requests
from django.contrib import messages
from .verifications import verify


def dealsView(request):
  template_name = 'deals/main.html'

  data = {
      'API_DEALS': os.getenv('API') + '/deals',
  }
  return render(request, template_name, data)

def handle_uploaded_file(file, file_path):
   with open(file_path, 'wb') as destination:
      for chunk in file.chunks():
        destination.write(chunk)

def dealsDetailView(request, pk):
  if request.user.is_authenticated == False or request.user.group != 'business':
    return redirect('login-view')
  
  template_name = 'deals/detail.html'
  deal = Deal.objects.get(id=pk)
  MEDIA_ROOT = settings.MEDIA_ROOT
  MEDIA_URL = settings.MEDIA_URL
  URL = os.getenv('URL')


  if request.method == 'POST':
    document = request.FILES.get('document')
    if document:
      name = document.name + datetime.datetime.now().strftime("_%Y%m%d%H%M%S")
      file_path = os.path.join(MEDIA_ROOT, 'scanqr', name)
      if not os.path.exists(MEDIA_ROOT + '/scanqr'):
        os.makedirs(MEDIA_ROOT + '/scanqr')
      handle_uploaded_file(document, file_path)
      QRAPI = 'https://api.qrserver.com/v1/read-qr-code/?fileurl='
      APIR = QRAPI + URL + '/' + MEDIA_URL + 'scanqr/' + name
      response = requests.get(APIR).text
      print(response)
      respData = json.loads(response)
      username = respData[0]['symbol'][0]['data']
      if verify(username) == False:
        messages.error(request, "Sorry, you don't meet the criteria!")
      else:
        messages.success(request, "Deal for " + username + " has been successfully activated!")

    return redirect('deals-view')

  data = {
        'deal':deal
  }
  return render(request, template_name, data)