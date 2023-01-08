from django.shortcuts import render, redirect
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from tricyhelp.forms import *
from django.contrib import messages
from tricyhelp_database import settings
from django.core.mail import send_mail

# Create your views here.

@method_decorator(login_required, name='dispatch')
class ComplaintView(View):
    def get(self, request):
        form = ComplaintInformationForm()
        form_2 = TricycleInformationForm()
        form_3 = IncidentInformationForm()
        return render(request, 'store/complaint_form.html', {'form': form,'form_2':form_2,'form_3':form_3})

    def post(self, request):
        form = ComplaintInformationForm(request.POST)
        form_2 = TricycleInformationForm(request.POST)
        form_3 = IncidentInformationForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            cname = form.cleaned_data['cname']
            address = form.cleaned_data['address']
            phone_number = form.cleaned_data['phone_number']
            
        if form_2.is_valid():
            dname = form_2.cleaned_data['dname']
            zone = form_2.cleaned_data['zone']
            d_address = form_2.cleaned_data['d_address']
            plate_number = form_2.cleaned_data['plate_number']
            operator_number = form_2.cleaned_data['operator_number']

        if form_3.is_valid():
            accident_date = form_3.cleaned_data['accident_date']
            accident_time = form_3.cleaned_data['accident_time']
            accident_place = form_3.cleaned_data['accident_place']
            violation_type = form_3.cleaned_data['violation_type']
            complaint_description = form_3.cleaned_data['complaint_description']
            complaint_evidence = form_3.cleaned_data['complaint_evidence']
        
        subject = 'A user has submitted a report!'
        message = 'Greetings' + '\nPlease check the administrator panel for the details of the report and review it.'
        from_email = settings.DEFAULT_FROM_EMAIL
        to_list = [settings.EMAIL_HOST_USER]
        send_mail(subject,message,from_email,to_list,fail_silently=True)
        reg = ComplaintInformation(user=user, cname=cname, address=address, phone_number=phone_number, dname=dname, zone=zone, d_address=d_address, plate_number=plate_number, operator_number=operator_number ,accident_date=accident_date, accident_time=accident_time, accident_place=accident_place, violation_type=violation_type  ,complaint_description=complaint_description, complaint_evidence=complaint_evidence)
        reg.save()
        messages.success(request, "Complaint Submitted!")
        return redirect('tricyhelp:complaints')

@login_required
def complaints(request):
    complaint = ComplaintInformation.objects.filter(user=request.user)
    descriptions = ComplaintInformation.objects.filter(user=request.user)
    verification_accepted = ComplaintInformation.objects.filter(user=request.user, verification="Accepted")
    verification_reviewing = ComplaintInformation.objects.filter(user=request.user, verification="Reviewing")
    verification_declined = ComplaintInformation.objects.filter(user=request.user, verification="Declined")
    context = {
        'complaint': complaint,
        'descriptions': descriptions,
        'verification_accepted': verification_accepted,
        'verification_reviewing': verification_reviewing,
        'verification_declined': verification_declined,
    }
    return render(request, 'store/complaints.html', context)

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, 'store/edit-profile.html', {'form':form})

    def post(self, request):
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user=request.user
            cname=form.cleaned_data['cname']
            address=form.cleaned_data['address']
            phone_number=form.cleaned_data['phone_number']
            profile_picture=form.cleaned_data['profile_picture']
            reg = Profile(user=user,cname=cname,address=address,phone_number=phone_number,profile_picture=profile_picture)
            reg.save()
            messages.success(request,"Successfully Profile Edit!")
        return redirect('tricyhelp:profile')

@login_required
def profile(request):
    informations = Profile.objects.filter(user=request.user)
    context = {
        'informations':informations
    }
    return render(request,'account/profile.html',context)

@method_decorator(login_required, name='dispatch')
class ContactView(View):
    def get(self, request):
        form = ContactUsForm()
        return render(request, 'store/contact.html',{'form':form})

    def post(self, request):
        form = ContactUsForm(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['fname']
            email_address = form.cleaned_data['email_address']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            reg = ContactUs(fname=fname,email_address=email_address,subject=subject,message=message)
            reg.save()
        return redirect('tricyhelp:profile')
