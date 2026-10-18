from django.db import models
from django.contrib.auth.models import User

# makemigrations= create changes on models & store in file
# migrate = apply pending changes created makemigration tables in database

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField(max_length=2000)
    date=models.DateField()
    
    def __str__(self):
        return self.email

# complain id ke liye
class Complain(models.Model):
    name=models.CharField(max_length=122)
    email=models.EmailField(max_length=254)
    phone=models.CharField(max_length=15)
    
    complain_type = models.CharField(
    max_length=100,
    choices=[
        ("theft", "Theft"),
        ("fraud", "Fraud"),
        ("missing", "Missing Person"),
        ("harassment", "Harassment"),
        ("other", "Other"),
    ]
    )
    
    location=models.CharField(max_length=255)
    incident_date=models.DateField()
    description=models.TextField()
    evidence=models.FileField(upload_to="evidence/",blank=True,null=True)
    
    # logged-in user
    user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    related_name="complaints",
    null=True,
    blank=True
)
    
    # professional complain Id
    complaint_id = models.CharField(
    max_length=30,
    unique=True,
    blank=True
    )
    status = models.CharField(
    max_length=30,
    default="Submitted",
    choices=[
        ("Submitted", "Submitted"),
        ("Under Review", "Under Review"),
        ("Investigation", "Investigation"),
        ("Resolved", "Resolved"),
        ("Rejected", "Rejected"),
    ]
)
    def __str__(self):
            return self.complaint_id or self.phone

# Next court or vakil