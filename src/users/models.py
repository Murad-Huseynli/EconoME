import os
from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
import qrcode
from datetime import datetime, timedelta

class QRCode(models.Model):
    code = models.ImageField(upload_to='qr_codes/')
    expirationDate = models.DateTimeField(null=True)

    def getCode(self):
        return self.code
    
    def getExpirationDate(self):
        return self.expirationDate
    
    def setCode(username):
        pass
    
    def setExpirationDate(self, expirationDate):
        self.expirationDate = expirationDate
        self.save()


class User(AbstractUser):
    SEXES = (
        ('Man', 'Man'),
        ('Woman', 'Woman'),
    )
        
    mobileNumber = models.CharField(max_length=25, default='')
    country = models.CharField(max_length=50, default='')
    city = models.CharField(max_length=50, default='')
    university = models.CharField(max_length=50, default='')
    sex =  models.CharField(max_length=20, choices=SEXES)
    groups = models.ManyToManyField(
        Group,
        verbose_name="groups",
        blank=True,
        help_text=
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ,
        related_name="user_groups",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name="user permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        related_name="user_groups",
        related_query_name="user",
    )

    def updateProfile(self):
        pass

    def getFirstName(self):
        return self.first_name
    
    def getLastName(self):
        return self.last_name
    
    def getEmail(self):
        return self.email
    
    def getCountry(self):
        return self.country
    
    def getCity(self):
        return self.city
    
    def getUniversity(self):
        return self.university
    
    def setFirstName(self, first_name):
        self.first_name = first_name
        self.save()
    
    def setLastName(self, last_name):
        self.first_name = last_name
        self.save()

    def setCountry(self, country):
        self.country = country
        self.save()
    
    def setCity(self, city):
        self.city = city
        self.save()

    def setPassword(self, password):
        self.set_password(password)
        self.save()

    def setEmail(self, email):
        self.email = email
        self.save()
    
    def setMobileNumber(self, mobileNumber):
        self.mobileNumber = mobileNumber
        self.save()


    

User._meta.get_field('groups').related_name = 'user_groups'
User._meta.get_field('user_permissions').related_name = 'user_permissions_list'
    
class RegularUser(User):
    img = models.ImageField(upload_to='profile/', null=True)
    group = models.CharField(max_length=50, default='')
    approval_document = models.FileField(upload_to='approval_documents/', null=True)
    qrCode = models.ForeignKey(QRCode, null=True, on_delete=models.PROTECT)
    is_approved = models.BooleanField(default=False)
    
    def getApprovalDocument(self):
        return self.approval_document
    
    def getQrCode(self):
        return self.qrCode
    
    def getImg(self):
        return self.img
    
    def getGroup(self):
        return self.group

    def setGroup(self, group):
        self.group = group
        self.save()
    
    def setQrCode(self, qrCode):
        self.qrCode = qrCode
        self.save()
    
    def addQrCode(self):
        username = self.username
        codeQR = qrcode.make(username)
        codeQR.save('qrCode' + username + '.jpg')
        with open('qrCode' + username + '.jpg', 'rb') as f:
            content = ContentFile(f.read())
            default_storage.save('qr_codes/qrCode' + username + '.jpg', content)
        url = default_storage.url('qr_codes/qrCode' + username + '.jpg')
        expiration_date = datetime.now() + timedelta(days=30)
        newCode = QRCode.objects.create(code=url, expirationDate=expiration_date)
        self.qrCode = newCode
        self.save()
        os.remove('qrCode' + username + '.jpg')

    def setImg(self, img):
        self.img = img
        self.save()

    def setApprovalDocument(self, approval_document):
        self.approval_document = approval_document
        self.save()
    
    def setApprove(self):
        self.is_approved = True
        self.addQrCode()
        self.save()




