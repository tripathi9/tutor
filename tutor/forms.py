from django.forms import ModelForm
from django import forms
from django.contrib.admin import widgets
from django.contrib.admin.widgets import AdminDateWidget
from .models import*



class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password',
                          widget=forms.PasswordInput())

    class Meta:
      model = Account
      fields=('usertype', 'firstname', 'lastname', 'email', 'password', 'mobile', 'city', 'state', 'pincode', 'profilepicture')

class ForgotPasswordForm(forms.ModelForm):
    email = forms.EmailField(label='Enter your registered email')
    class Meta:
        model = Account
        fields=('email',)

# class SearchForm(forms.ModelForm):
#     searchbox = forms.CharField(placeholder="Search tutor by skills")
class TravelPolicyForm(forms.ModelForm):

    class Meta:
        model = Travel
        fields=('travel',)


class RatePolicyForm(forms.ModelForm):

    class Meta:
        model = Rate
        fields=('rate',)



class UserProfileForm(forms.ModelForm):
    email = forms.EmailField(label='Email')
    class Meta:
      model = Account
      fields=('usertype', 'firstname', 'lastname', 'email', 'mobile', 'city', 'state', 'pincode', 'profilepicture')

class ExpertiseForm(forms.ModelForm):
    class Meta:
      model = Expertise
      fields=('expert', 'level')


class QualificationsForm(forms.ModelForm):
    # HighestQualification = forms.ChoiceField(label='Highest Qualification' , choices='standards')
    experience = forms.IntegerField(label='Experience(years)')
    university = forms.CharField(label='university/board')

    class Meta:
      model = Qualifications
      fields=('highestQualification', 'university', 'stream', 'experience')


class TutorBioForm(forms.ModelForm):

    describe = forms.CharField(label='Enter your tagline')
    bio= forms.CharField(label='Write a professional personal statement', widget=forms.Textarea)


    class Meta:
      model = TutorBio
      fields=('describe', 'bio')
