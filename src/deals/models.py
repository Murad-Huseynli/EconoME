from django.db import models
from django.contrib.postgres.fields import ArrayField

class Business(models.Model):
    businessName = models.CharField(max_length=50, default='')
    address = ArrayField(models.CharField(max_length=40), default=list)
    logo = models.ImageField(upload_to='business/', null=True)
    
    def getBusinessName(self):
        return self.businessName
    
    def getAdresses(self):
        return ' '.join(self.address)

    def setBusinessName(self, name):
        self.businessName = name
        self.save()

    def setAddress(self, address):
        self.address = address
        self.save()
    
    def setLogo(self, logo):
        self.logo = logo
        self.save()

    def manageDeals():
        pass
    
    def viewAnalytics():
        pass
    
    def scanQRCode(self, qrCode):
        pass

    def __str__(self):
        return self.getBusinessName()



class Deal(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    preview = models.ImageField(upload_to='preview/', null=True)
    termsConditions = models.CharField(max_length=100)
    startDate = models.DateField(null=True)
    endDate = models.DateField(null=True)
    isActive = models.BooleanField(default=False)
    discountRateByGroup = models.JSONField(default={"":""})
    offeredBy = models.ForeignKey(Business, on_delete=models.CASCADE, null=True)
    
    def getTitle(self):
        return self.title
    
    def getDescription(self):
        return self.description
    
    def getTermsConditions(self):
        return self.termsConditions
    
    def getDiscountRateByGroup(self, group):
        return self.discountRateByGroup[group]
    
    def getStartDate(self):
        return self.getStartDate
    
    def getEndDate(self):
        return self.getEndDate
    
    def getIsActive(self):
        return self.getIsActive
    
    def getOfferedBy(self):
        return self.offeredBy.getBusinessName()
    
    def setTitle(self, title):
        self.title = title
        self.save()
    
    def setDescription(self, description):
        self.description = description
        self.save()

    def setTermsConditions(self, terms):
        self.termsConditions = terms
        self.save()

    def setDiscountRateByGroup(self, group, discountRate):
        self.discountRateByGroup[group] = discountRate
        self.save()

    def setStartDate(self, date):
        self.startDate = date
        self.save()

    def setEndDate(self, date):
        self.endDate = date    
        self.save()
    
    def setIsActive(self, status):
        self.isActive = status
        self.save()
    
    def setOfferedByName(self, business_name):
        business = Business.objects.get(businessName=business_name)
        self.offeredBy = business
        self.save()

    def setOfferedBy(self, business):
        self.offeredBy = business
        self.save()


