from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

# Create your models here.
class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        # Ensure that an email address is set
        if not email:
            raise ValueError('Users must have a valid e-mail address')

        # Ensure that a username is set

        account = self.model(
            usertype=kwargs.get('usertype', None),
            email=self.normalize_email(email),
            firstname=kwargs.get('firstname', None),
            lastname=kwargs.get('lastname', None),
            mobile=kwargs.get('mobile', None),
            city=kwargs.get('city', None),
            state=kwargs.get('state', None),
            pincode=kwargs.get('pincode', None),
            profilepicture=kwargs.get('profilepicture', None),
        )
        account.set_password(password)
        account.save()

        return account





class Account(AbstractBaseUser):
    account_type = (
    ("Student", "Student"),
    ("Tutor", "Tutor"),
    )

    usertype = models.CharField(max_length=8,
                  choices=account_type, default="Student"
                 )

    email = models.EmailField(unique=True)

    firstname = models.CharField(max_length=50, blank=True, validators=[RegexValidator(r'^[a-zA-Z]*$', message='please Enter A valid Name must have only alphabets', code='Invalid Name')])
    lastname = models.CharField(max_length=50, blank=True)
    mobile = models.CharField(('Mobile'),max_length=10,blank=True,unique=False)
    city= models.CharField(max_length=20)
    state = models.CharField(max_length=100)
    pincode = models.IntegerField(null=True,blank=True, default=0)
    profilepicture = models.ImageField(null=True, blank=True, max_length=5000)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    is_admin = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname']


    def __unicode__(self):
        return '%s'%(self.firstname)

    def get_full_name(self):
        """ User create Base Manager"""
        return (self.firstname +" " + self.lastname)

    def get_mobile(self):
        """ User create Base Manager"""
        return (self.mobile)

    def address(self):
            """ User create Base Manager"""
            return (self.city +","+self.state)

    def get_usertype(self):
                """ User create Base Manager"""
                return (self.usertype)







class Expertise(models.Model):
    user=models.ManyToManyField(Account)
    expert_in = (
        ("English", "English"),
        ("Maths", "Maths"),
        ("Physics", "Physics"),
        ("Chemistry", "Chemistry"),
        ("Biology", "Biology"),
        ("Computer", "Computer"),
        ("SocialScience", "SocialScience"),
        )

    expert = models.CharField(max_length=12,
                      choices=expert_in, default="English"
                     )
    levels_upto=(
    ("Primary", "Primary"),
    ("HighSchool", "HighSchool"),
    ("College", "College"),
    )
    level = models.CharField(max_length=12,
                          choices=levels_upto, default="Primary"
                         )
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.expert



class Qualifications(models.Model):
    userid=models.ForeignKey(Account, on_delete=models.CASCADE)
    standards=(
        ("HighSchool", "HighSchool"),
        ("Intermediate", "Intermediate"),
        ("BacheleorDegree", "BacheleorDegree"),
        ("MasterDegree", "MasterDegree"),
        ("Doctorate", "Doctorate"),
        )
    highestQualification = models.CharField(max_length=20,
                          choices=standards, default="HighSchool"
                         )
    stream_in=(
            ("ComputerScience", "ComputerScience"),
            ("informationTechnology", "informationTechnology"),
            ("Maths", "Maths"),
            ("Physics", "Physics"),
            ("Chemistry", "Chemistry"),
            ("Meidcal", "Meidcal"),
            ("Arts", "Arts"),
            ("Accounts", "Accounts"),
            ("Economics", "Economics"),
            )
    stream=models.CharField(max_length=20,
                          choices=stream_in, default="ComputerScience"
                         )
    university =  models.CharField(max_length=50, blank=True)
    experience =  models.IntegerField(null=True,blank=True, default=0)
class TutorBio(models.Model):
    userid=models.ForeignKey(Account, on_delete=models.CASCADE)
    describe=models.CharField(max_length=20, blank=True)
    bio=models.TextField()
