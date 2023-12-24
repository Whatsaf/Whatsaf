from django.db import models
from django.contrib.auth.models import User

# Database Codes
class Contact(models.Model):
    Name = models.CharField(max_length=100, blank=False)
    Email = models.EmailField(max_length=100, blank=False)
    Subject = models.CharField(max_length=500, blank=False)
    Message = models.TextField(max_length=2000, blank=False)

    def __str__(self) -> str:
        return f"{self.Name} | {self.Subject}"

class UserDetail(models.Model):
    User = models.ForeignKey(User, related_name="UserDetailsExtra", on_delete=models.CASCADE)
    Phone = models.CharField(max_length=200, blank=False)
    DOB = models.DateField(default="")
    Country = models.CharField(default="", max_length=100)
    ProfilePhoto = models.ImageField(upload_to="ProfilePhoto", default="ProfilePhoto/Default.png")
    OTP1 = models.CharField(max_length=100, blank=True, default="")
    OTP2 = models.CharField(max_length=100, blank=True, default="")
    Verification = models.BooleanField(default=False)
    Premium = models.BooleanField(default=False)
    AlphaPremium = models.BooleanField(default=False)
    GigaPremium = models.BooleanField(default=False)
    Trial = models.BooleanField(default=False)
    BrowserID = models.CharField(max_length=100, default="")
    Active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.User.username} | {self.User.first_name}"

class FAQ(models.Model):
    User = models.ForeignKey(User, related_name="UserFAQ", on_delete=models.CASCADE)
    Question = models.TextField(max_length=10000)
    Answer = models.TextField(max_length=100000)

    def __str__(self) -> str:
        return self.Question

class Feature(models.Model):
    Name = models.CharField(max_length=1000)
    Short = models.CharField(max_length=1000, default="")
    Desc = models.TextField(max_length=1000)
    Link = models.CharField(max_length=100)
    Image = models.CharField(max_length=1000)
    Stable = models.BooleanField(default=False)
    AlphaPremium = models.BooleanField(default=False)
    GigaPremium = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.Name

class Newsletter(models.Model):
    Email = models.EmailField(max_length=100)

    def __str__(self) -> str:
        return self.Email

class UserWhatsAppDetail(models.Model):
    conC = [
        ("Contacts", "Contacts")
    ]
    bloC = [
        ("BlockedContacts", "BlockedContacts")
    ]
    User = models.ForeignKey(User, related_name = "UserWhatsAppDetail", on_delete=models.CASCADE)
    UserName = models.CharField(max_length = 500, default = "")
    UserPP = models.CharField(max_length = 500, default = "")
    UserAbout = models.CharField(max_length = 500, default = "")
    UserLastSeenSetting = models.BooleanField(default = False)
    UserOnlineStatusSetting = models.BooleanField(default = False)
    UserReadRecipents = models.BooleanField(default = False)
    UserDisapperingMessageSetting = models.BooleanField(default = False)
    UserBlockedContacts = models.CharField(max_length = 500, choices = bloC, default = "")
    UserContact = models.CharField(max_length = 500, choices = conC, default = "")
    UserContactPP = models.CharField(max_length = 500, default = "")

    @classmethod
    def update_UserContact(cls, new_choices):
        cls._meta.get_field('UserContact').choices += new_choices
    
    @classmethod
    def update_UserBlockedContact(cls, new_choices):
        cls._meta.get_field('UserBlockedContacts').choices += new_choices
    
    def __str__(self) -> str:
        return self.User.first_name