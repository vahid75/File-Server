from django.shortcuts import render , redirect
from . import forms
from django.contrib import messages
from . import utils
from django.conf import settings
from django.http import HttpResponse
import os 

def upload_file(request):
    form = forms.Upload_Form()
    if request.method == "POST":        
        form = forms.Upload_Form(request.POST, request.FILES)

        if form.is_valid():
            uploaded_file = request.FILES.get("uploaded_file")
            utils.saving_file(uploaded_file)
            messages.success(request  , 'file uploaded successfully')
            return redirect('upload_file')
    else:
        form = forms.Upload_Form()

    form_context = {"form": form}
    return render(request, "upload.html", context=form_context)


def register_via_ip(request):    

    ip_address_file_path = settings.CLIENT_IP_ADDRESS_FILE    
    with open(ip_address_file_path , 'r+') as file:
        registered_ip_addresses = utils.ip_list_generator(file)
        if request.client_ip_address  not in registered_ip_addresses:
            file.write(request.client_ip_address)
            file.write('\n')

    # context = {
    #     'ip_address' : request.client_ip_address
    # }
    # return render(request, "registration.html", context=context)
    return redirect('home')
    

def home(request):    

    context = {
        'ip_address' : request.client_ip_address
    }
    return render(request, "home.html", context=context)