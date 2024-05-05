from django.contrib import admin
from .models import QRCode, User, RegularUser

admin.site.register(QRCode)
admin.site.register(User)
admin.site.register(RegularUser)

