from django.db import models
from django.contrib.auth.models import User
# Create your models here.

VIOLATION_CHOICES = (
    ('Contracting Passenger','Contracting Passenger'),
    ('Overcharging Fare','Overcharging Fare'),
    ('Arrogant Discourteous Driver','Arrogant Discourteous Driver'),
    ('Refusal To Convey Passenger','Refusal To Convey Passenger'),
    ('Hit And Run','Hit And Run'),
    ('Threatening Passenger','Threatening Passenger'),
    ('Reckless Driving','Reckless Driving'),
    ('Discriminating Againts Passenger','Discriminating Againts Passenger'),
    ('Refusal To Grant Discount','Refusal To Grant Discount'),
)

VERIFICATION_CHOICES = (
    ('Accepted','Accepted'),
    ('Reviewing','Reviewing'),
    ('Declined','Declined'),
)

class ComplaintInformation(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    cname = models.CharField(max_length=150, verbose_name="Complete Name", blank=False)
    address = models.CharField(max_length=150, verbose_name="Complete Address", blank=False)
    phone_number = models.CharField(max_length=11, verbose_name="Phone Number", blank=False)
    dname = models.CharField(max_length=150, verbose_name="Driver Name/Operator Name", blank=False)
    zone = models.CharField(max_length=100, verbose_name="Zone Address", blank=False)
    d_address = models.CharField(max_length=150, verbose_name="Driver/Operator Complete Address", blank=False)
    plate_number = models.CharField(max_length=50, verbose_name="Plate Number", blank=False)
    operator_number = models.CharField(max_length=13, default="+63", verbose_name="Operator Number", blank=False)
    accident_date = models.DateField(verbose_name="Date of Accident")
    accident_time = models.TimeField(verbose_name="Time of Accident")
    accident_place = models.CharField(max_length=150, verbose_name="Place of Accident", blank=False)
    violation_type = models.CharField(max_length=150, choices=VIOLATION_CHOICES, verbose_name="Violation Type")
    complaint_description = models.TextField(verbose_name="Complaint Description", blank=False)
    complaint_evidence = models.ImageField(upload_to='evidences',blank=True, null=True, verbose_name="Evidence Image")
    verification = models.CharField(max_length=100, choices=VERIFICATION_CHOICES, default="Reviewing" ,verbose_name="Verification")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")

    def __str__(self):
        return self.complaint_description

    class Meta:
        verbose_name_plural = "Complaint List"

class ContactUs(models.Model):
    fname = models.CharField(max_length=150, verbose_name="Complete Name", blank=False)
    email_address = models.EmailField(verbose_name="Email Address", blank=False)
    subject = models.CharField(max_length=100, verbose_name="Subject Message", blank=False)
    message = models.TextField(verbose_name="Message")

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name_plural = "Contact List"

class Profile(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    cname = models.CharField(max_length=150, verbose_name="Complete Name", blank=False)
    address = models.CharField(max_length=150, verbose_name="Complete Address", blank=False)
    phone_number = models.CharField(max_length=13, default="+63", verbose_name="Phone Number", blank=False)
    profile_picture = models.ImageField(upload_to='profile_pictures',blank=True, null=True, verbose_name="Profile Picture")

    def __str__(self):
        return self.cname