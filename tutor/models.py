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
    def create_superuser(self, email, password=None, **kwargs):
        # Ensure that an email address is set



        account = self.create_user(
                   email,
                   password=password,
                   usertype=kwargs.get('usertype', None),
                   firstname=kwargs.get('firstname', None),
                   lastname=kwargs.get('lastname', None),
                   mobile=kwargs.get('mobile', None),
                   city=kwargs.get('city', None),
                   state=kwargs.get('state', None)

               )


        account.is_admin = True
        account.set_password(password)
        account.save(using=self._db)

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
    REQUIRED_FIELDS = ['firstname', 'lastname', 'mobile', 'city', 'state', 'usertype']


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

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    def get_short_name(self):
    # The user is identified by their email address
        return self.firstname

class Stream(models.Model):
    streamid = models.AutoField(primary_key=True)
    stream = models.CharField(max_length=25)
    def __str__(self):
        return self.stream




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

    stream=models.ForeignKey(Stream, on_delete=models.CASCADE)
    university =  models.CharField(max_length=50, blank=True)
    experience =  models.IntegerField(null=True,blank=True, default=0)



class TutorBio(models.Model):
    userid=models.ForeignKey(Account, on_delete=models.CASCADE)
    describe=models.CharField(max_length=20, blank=True)
    bio=models.TextField()


class Subject(models.Model):
    subjectid = models.AutoField(primary_key=True)
    subject =  models.CharField(max_length=50)

    def __str__(self):
        return self.subject

class Categories(models.Model):

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default="select")
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category
class Expertise(models.Model):
    user=models.ManyToManyField(Account)
    expert = models.ForeignKey(Subject, on_delete=models.CASCADE, default="select")
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

    # def __str__(self):
    #     return self.expert

class Travel(models.Model):
    user= models.ForeignKey(Account, on_delete=models.CASCADE)
    travel_policy=(
        ("I only teach from home", "I only teach from home"),
        ("1 miles", "1 miles"),
        ("2 miles", "2 miles"),
        ("3 miles", "3 miles"),
        ("4 miles", "4 miles"),
        ("5 miles", "5 miles"),
        ("8 miles", "8 miles"),
        ("10 miles", "10 miles"),
        ("12 miles", "12 miles"),
    )
    travel = models.CharField(max_length=25,
                              choices=travel_policy, default="Select"
                             )
class Rate(models.Model):
        user= models.ForeignKey(Account, on_delete=models.CASCADE)
        rate = models.IntegerField()
