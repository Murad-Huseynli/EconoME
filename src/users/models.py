from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models
import qrcode

class QRCode(models.Model):
    code = models.ImageField(upload_to='qr_codes/')
    expirationDate = models.DateTimeField(null=True)

    def getCode(self):
        return self.code
    
    def getExpirationDate(self):
        return self.expirationDate
    
    def setCode(self, username):
        codeQR = qrcode.make(username).read()
        self.code.save('qrcode' + username, codeQR)
        self.save()
    
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
    
    def setGroup(self, group):
        self.group = group
        self.save()
    
    def setQrCode(self, qrCode):
        self.qrCode = qrCode
        self.save()
    
    def addQrCode(self):
        qrcode = QRCode.objects.create()
        qrcode.setCode(self.username)

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




