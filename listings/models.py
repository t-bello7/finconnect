from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Listings(models.Model):
    COMPANY = 'CO'
    MICROFINANCE_BANK = 'MB'
    COOPERATIVE_SOCIETIES = 'CS'
    FINANCIAL_BANKING = 'FB'
    INSURANCE_COMPANIES = 'IC'


    INSTITUTION_CHOICES = [
        (COMPANY, 'Company'),
        (MICROFINANCE_BANK , 'Microfinance Bank'),
        (COOPERATIVE_SOCIETIES, 'Cooperative Societies'),
        (FINANCIAL_BANKING, 'Financial Banking'),
        (INSURANCE_COMPANIES, 'Insurance Companies')
    ]
    list_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    name = models.CharField(max_length=100)
    instiution = models.CharField(max_length=2, choices=INSTITUTION_CHOICES, default=COMPANY)
    address = models.CharField(max_length=150)
    list_image = models.ImageField(upload_to='listing', null=True,blank=True)
    address = models.CharField(max_length=255, null=True)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    close_time = models.TimeField(auto_now=False, auto_now_add=False)
    is_saturday_available = models.BooleanField(default=False)
    start_time_sat = models.TimeField(auto_now=False, auto_now_add=False)
    close_time_sat = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural='Listings'

class Plans(models.Model):
    plan_id = models.ForeignKey(Listings, on_delete=models.CASCADE ,related_name='listings')
    name = models.CharField(max_length=100)
    plan_image = models.ImageField(upload_to='plans',null=True, blank=True)
    price  = models.FloatField()
    freqency_type = models.CharField(max_length=15)
    percentage_return = models.FloatField()
    max_amount = models.FloatField()
    min_amount = models.FloatField()



    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name_plural='Plans'