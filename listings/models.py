from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Listings(models.Model):
    #change id to uuid
        # id = models.UUIDField(primary_key=True, default=uuid4,
        #                   unique=True, editable=False)
    MICROFINANCE_BANK = 'MB'
    COOPERATIVE_SOCIETIES = 'CS'
    FINANCIAL_BANKING = 'FB'
    INSURANCE_COMPANIES = 'IC'


    INSTITUTION_CHOICES = [
        (MICROFINANCE_BANK , 'Microfinance Bank'),
        (COOPERATIVE_SOCIETIES, 'Cooperative Societies'),
        (FINANCIAL_BANKING, 'Financial Banking'),
        (INSURANCE_COMPANIES, 'Insurance Companies')
    ]
    list_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    name = models.CharField(max_length=100)
    institution = models.CharField(max_length=2, choices=INSTITUTION_CHOICES)
    address = models.CharField(max_length=150)
    description = models.TextField()
    list_image = models.ImageField(upload_to='listing', null=True,blank=True)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    close_time = models.TimeField(auto_now=False, auto_now_add=False)
    is_saturday_available = models.BooleanField(default=False)
    start_time_sat = models.TimeField(auto_now=False, auto_now_add=False)
    close_time_sat = models.TimeField(auto_now=False, auto_now_add=False)

    @property
    def get_microfinance_count(self):
        return Listings.objects.all().filter(institution='MB').count()
    
    @property
    def get_cooperative_count(self):
        return Listings.objects.all().filter(institution='CS').count()
    
    @property
    def get_financial_count(self):
        return Listings.objects.all().filter(institution='FB').count()

    @property
    def get_insurance_count(self):
        return Listings.objects.all().filter(institution='IC').count()

    # To pass it to the view you can add it to the context in the views.py as count = Feedback.get_feedback_count()
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("list-detail", kwargs={'pk': str(self.pk)})

    class Meta:
        verbose_name_plural='Listings'
    

class Plans(models.Model):

    plan_id = models.ForeignKey(Listings, on_delete=models.CASCADE ,related_name='listings')
    plan_type = models.CharField(max_length=266)
    name = models.CharField(max_length=100)
    plan_image = models.ImageField(upload_to='plans',null=True, blank=True)
    price  = models.FloatField()
    rate = models.CharField(max_length=15)
    percentage_return = models.FloatField()
    max_amount = models.FloatField()
    min_amount = models.FloatField()



    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name_plural='Plans'

class PlansCategory(models.Model):
    # LOAN = 'LN'
    # SAVINGS = 'SS'
    # INVESTMENT = 'IM'
    # PENSION = "PS"
    # INSURANCE = 'IS'
    name = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural='Plans Categories'