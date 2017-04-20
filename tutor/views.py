from django.shortcuts import render
from tutor.forms import *
from django.contrib.auth.models import User
from .models import*
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, logout, login
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpResponseRedirect, HttpResponseBadRequest, HttpResponseNotAllowed
from django.contrib import messages


def main(request):
    try:
        sub= Subject.objects.all()
    except Subject.DoesNotExist:
        sub=Subject.objects.none
    try:
        acc= Account.objects.values('city').distinct()
    except Account.DoesNotExist:
        acc=Account.objects.none
    context={
    "sub":sub,
    "acc":acc,
    "title":"WELCOME"
    }

    return render(request, 'tutor/base.html', context)


def profile(request):
    user=request.user
    if user.is_authenticated:

        if user.usertype == "Tutor":

            subject=Expertise.objects.filter(user=user.id)
            try:
                qualify= Qualifications.objects.get(userid=user.id)
            except Qualifications.DoesNotExist:
                qualify = Qualifications.objects.none
            try:
                tbio = TutorBio.objects.get(userid=user.id)

            except TutorBio.DoesNotExist:
                tbio = TutorBio.objects.none
            try:
                trav = Travel.objects.get(user=user.id)
            except Travel.DoesNotExist:
                trav = Travel.objects.none

            try:
                rat = Rate.objects.get(user=user.id)
            except Rate.DoesNotExist:
                rat = Rate.objects.none


            usertype="Student"

            list1=Account.objects.exclude(usertype=usertype)
            context={"list":list1,
            "subject":subject,
            "qualify" : qualify,
            "tbio":tbio,
            "title":usertype,
            "trav":trav,
            "rat":rat
            }
            return render(request, 'tutor/profile.html', context)
        else:

            usertype="Student"

            list1=Account.objects.exclude(usertype=usertype)
            context={"list":list1,
            "title":usertype
            }
            return render(request, 'tutor/profile.html', context)
    else:
        return render(request, 'tutor/unauthorisedUser.html', {})



@csrf_exempt
def manageprofile(request):

    expert=Expertise()
    user=request.user
    userid=user.id
    profile=get_object_or_404(Account, id=userid)
    form = UserProfileForm(request.POST or None, request.FILES or None, instance=profile)
    if form.is_valid():
            profile=form.save(commit=False)
            print (form.cleaned_data.get("first_name"))
            profile.save()
            context={
            "profile":profile,
            "expert":expert,
            "form":form,

        }
            return HttpResponseRedirect('/accounts/profile')
    else:
        form = UserProfileForm(request.POST or None, request.FILES or None, instance = profile)
        context={
        "profile":profile,
        "form":form,
    }
    return render(request, 'tutor/userprofile.html', context)


@csrf_exempt
def user_register(request):
    form = UserRegisterForm(request.POST or None, request.FILES or None)
    params = request.POST
    if form.is_valid():
        user = Account.objects.create_user(usertype=form.cleaned_data['usertype'],password=form.cleaned_data['password'],email=form.cleaned_data['email'],
        firstname=form.cleaned_data['firstname'],lastname=form.cleaned_data['lastname'],mobile=form.cleaned_data['mobile'],
        city=form.cleaned_data['city'],state=form.cleaned_data['state'],pincode=form.cleaned_data['pincode'],profilepicture=form.cleaned_data['profilepicture'])
        new_user = authenticate(email=form.cleaned_data['email'],
                                    password=form.cleaned_data['password'],
                                    )
        login(request, new_user)


        return HttpResponseRedirect('/accounts/profile')
    else:
        print(form.errors)
    context = {
        "form":form,
        }
    return render(request, 'tutor/register.html', context)


def add_expertise(request):
    use=request.user
    if use.is_authenticated:
        a=Account.objects.get(id=use.id)
        form = ExpertiseForm(request.POST or None)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            instance.user.add(a)
            # messages.success(request,"Succesfuly create")
            return HttpResponseRedirect('/accounts/profile')
            # return render(request, 'check/profile.html', context)

        else:
            print("invalid form")
            print(form.errors)
            # messages.error(request, "Not able to  create")
            context = {
            "form":form,
            }
            return render(request, 'tutor/expertise.html', context)
    else:
        return render(request, 'tutor/unauthorisedUser.html', {})


def add_qualifications(request):
    use=request.user
    if use.is_authenticated:
        try:
            qualification = Qualifications.objects.get(userid=use.id)
            form = QualificationsForm(request.POST or None, instance=qualification)
            if form.is_valid():
                instance=form.save(commit=False)
                instance.userid=request.user
                instance.save()

                # messages.success(request,"Succesfuly create")
                return HttpResponseRedirect('/accounts/profile')
                # return render(request, 'check/profile.html', context)

            else:
                print("invalid form")
                print(form.errors)
        # messages.error(request, "Not able to  create")
            context = {
                "form":form,
                }
            return render(request, 'tutor/qualifications.html', context)
        except Qualifications.DoesNotExist:
                    form = QualificationsForm(request.POST or None)
                    if form.is_valid():
                        instance=form.save(commit=False)
                        instance.userid=request.user
                        instance.save()

                        # messages.success(request,"Succesfuly create")
                        return HttpResponseRedirect('/accounts/profile')
                        # return render(request, 'check/profile.html', context)

                    else:
                        print("invalid form")
                        print(form.errors)
                # messages.error(request, "Not able to  create")
                    context = {
                        "form":form,
                        }
                    return render(request, 'tutor/qualifications.html', context)
    else:
        return render(request, 'tutor/unauthorisedUser.html', {})



def add_Bio(request):
    use=request.user
    if use.is_authenticated:
        try:
            bio = TutorBio.objects.get(userid=use.id)
            form = TutorBioForm(request.POST or None, instance=bio)
            if form.is_valid():
                instance=form.save(commit=False)
                instance.userid=request.user
                instance.save()

                # messages.success(request,"Succesfuly create")
                return HttpResponseRedirect('/accounts/profile')
                # return render(request, 'check/profile.html', context)

            else:
                print("invalid form")
                print(form.errors)
                # messages.error(request, "Not able to  create")
            context = {
                "form":form,
                }
            return render(request, 'tutor/addBio.html', context)
        except TutorBio.DoesNotExist:
                    form = TutorBioForm(request.POST or None)
                    if form.is_valid():
                        instance=form.save(commit=False)
                        instance.userid=request.user
                        instance.save()

                        # messages.success(request,"Succesfuly create")
                        return HttpResponseRedirect('/accounts/profile')
                        # return render(request, 'check/profile.html', context)

                    else:
                        print("invalid form")
                        print(form.errors)
                # messages.error(request, "Not able to  create")
                    context = {
                        "form":form,
                        }
                    return render(request, 'tutor/addBio.html', context)

    else:
        return render(request, 'tutor/unauthorisedUser.html', {})

def tutorDetails(request, id=None):
        use=Account.objects.get(id=id)
        try:
           subject=Expertise.objects.filter(user=id)
        except Expertise.DoesNotExist:
            subject = Expertise.objects.none

        try:
            qualify= Qualifications.objects.get(userid=id)
        except Qualifications.DoesNotExist:
            qualify = Qualifications.objects.none
        try:
            tbio = TutorBio.objects.get(userid=id)

        except TutorBio.DoesNotExist:
            tbio = TutorBio.objects.none


        try:
            trav = Travel.objects.get(user=id)
        except Travel.DoesNotExist:
            trav = Travel.objects.none

        try:
            rat = Rate.objects.get(user=id)
        except Rate.DoesNotExist:
            rat = Rate.objects.none
# print (qualify.HighestQualification)

        context={
        "subject":subject,
        "qualify" : qualify,
        "tbio":tbio,
        "use":use,
        "trav":trav,
        "rat":rat
        }
        return render(request, 'tutor/tutorDetails.html', context)


@csrf_exempt
def forget_password(request):
    """
    retrieving Users password
    """
    form = ForgotPasswordForm(request.GET or None)
    context={"form":form}
    if form.is_valid():
        try:
            chk = Account.objects.get(email__iexact=form.cleaned_data['email'])
            print (chk)

        except Account.DoesNotExist:
            messages.info(request, 'email does not exist')
            return render(request, 'tutor/forgotpassword.html', context)
    return render(request, 'tutor/forgotpassword.html', context)

    # if chk:
    #     try:
    #
    #         send_mail('Password reset Instruction', 'Password resest Instruction', 'from@example.com', [user.Email], fail_silently=False)
    #         return JsonResponse({"status":"200", "ResponseMessage":"Email with Password reset Instructions has been sent to your registered Mail"})
    #     except BadHeaderError:
    #         print (hello)
    #         return JsonResponse({"status":"400", "ResponseMessage":"your registered Email, is not valid"})
    #

def travel_policy(request):
    use=request.user
    if use.is_authenticated:
        try:
            trav = Travel.objects.get(user=use.id)
            form = TravelPolicyForm(request.POST or None, instance=trav)
            if form.is_valid():
                instance=form.save(commit=False)
                instance.user=request.user
                instance.save()

                # messages.success(request,"Succesfuly create")
                return HttpResponseRedirect('/accounts/profile')
                # return render(request, 'check/profile.html', context)

            else:
                print("invalid form")
                print(form.errors)
                # messages.error(request, "Not able to  create")
            context = {
                "form":form,
                }
            return render(request, 'tutor/travelpolicy.html', context)
        except Travel.DoesNotExist:
                    form = TravelPolicyForm(request.POST or None)
                    if form.is_valid():
                        instance=form.save(commit=False)
                        instance.user=request.user
                        instance.save()

                        # messages.success(request,"Succesfuly create")
                        return HttpResponseRedirect('/accounts/profile')
                        # return render(request, 'check/profile.html', context)

                    else:
                        print("invalid form")
                        print(form.errors)
                # messages.error(request, "Not able to  create")
                    context = {
                        "form":form,
                        }
                    return render(request, 'tutor/travelpolicy.html', context)

    else:
        return render(request, 'tutor/unauthorisedUser.html', {})

def rate_policy(request):
    use=request.user
    if use.is_authenticated:
        try:
            rat = Rate.objects.get(user=use.id)
            form = RatePolicyForm(request.POST or None, instance=rat)
            if form.is_valid():
                instance=form.save(commit=False)
                instance.user=request.user
                instance.save()

                # messages.success(request,"Succesfuly create")
                return HttpResponseRedirect('/accounts/profile')
                # return render(request, 'check/profile.html', context)

            else:
                print("invalid form")
                print(form.errors)
                # messages.error(request, "Not able to  create")
            context = {
                "form":form,
                }
            return render(request, 'tutor/fee.html', context)
        except Rate.DoesNotExist:
                    form = RatePolicyForm(request.POST or None)
                    if form.is_valid():
                        instance=form.save(commit=False)
                        instance.user=request.user
                        instance.save()

                        # messages.success(request,"Succesfuly create")
                        return HttpResponseRedirect('/accounts/profile')
                        # return render(request, 'check/profile.html', context)

                    else:
                        print("invalid form")
                        print(form.errors)
                # messages.error(request, "Not able to  create")
                    context = {
                        "form":form,
                        }
                    return render(request, 'tutor/fee.html', context)

    else:
        return render(request, 'tutor/unauthorisedUser.html', {})




@csrf_exempt
def search_tutors(request):
    if request.method == 'GET':

        search_query = request.GET.get('search_box', None)
        obj = Account.objects.filter(expertise__expert__subject__contains=search_query).distinct()
        print(obj)
        context={
        "obj":obj
        }
        return render(request, 'tutor/tutors.html', context)

@csrf_exempt
def tutors_by_subject(request, subject=None):
        search_query = subject
        obj = Account.objects.filter(expertise__expert__subject__contains=search_query).distinct()
        print(obj)
        context={
        "obj":obj
        }
        return render(request, 'tutor/tutors.html', context)




def by_city(request):
        print ("search_query")
        # search_query = city
        # #
        # print(search_query)
        # obj = Account.objects.filter(city='Ghazibad')
        #
        # print ("hii")
        #
        # print(obj)
        # context={
        # "obj":obj
        # }
        # return render(request, 'tutor/tutors.html', context)





def logout_page(request):
    print("logout")
    logout(request)
    return HttpResponseRedirect('/')
