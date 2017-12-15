from django.shortcuts import render
from .models import PhoneBrand,PhoneModel
# Create your views here.

def model_detail(request,index):
    model=PhoneModel.objects.get(pk=index)
    return render(request,'model.html',{'model':model})

