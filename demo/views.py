from django.shortcuts import render
from .models import PhoneBrand,PhoneModel
# Create your views here.

def model_detail(request,index):
    model=PhoneModel.objects.get(pk=index)
    return render(request,'model.html',{'model':model})

# echo "# assignment1-django-models-ahsenakpinar" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git remote add origin https://github.com/IstanbulSehirUniversity2017Fall/assignment1-django-models-ahsenakpinar.git
# git push -u origin master