from django.shortcuts import render,redirect
from .models import PhoneBrand,PhoneModel,CategoryModel
from .forms import CategoryForm,BrandForm,PhoneForm
# Create your views here.

def model_detail(request,index):
    model=PhoneModel.objects.get(pk=index)
    return render(request,'model.html',{'model':model,'title':'Model Detail'})

def brand_detail(request,index):
    brand=PhoneBrand.objects.get(pk=index)
    model_list=PhoneModel.objects.filter(brand=brand)
    return render(request,'brand.html',{'brand':brand,'title':'Brand Detail','model_list':model_list})

def category_detail(request,index):
    category=CategoryModel.objects.get(pk=index)
    brand_list=PhoneBrand.objects.filter(cat_type=category)
    return render(request,'category.html',{'category':category,'title':'Category Detail','brand_list':brand_list})

def model_table(request):
    if request.method=='POST':
        item=PhoneModel.objects.get(pk=request.POST['id'])
        form = PhoneForm(data=request.POST,instance=item)
        if form.is_valid():
            form.save()
        return redirect('http://127.0.0.1:8000/demo/model/')
    else:
        model_list=PhoneModel.objects.all()
        model_forms=[]
        for model in model_list:
            form = PhoneForm(instance=model)
            model_forms.append((model,form))
        return render(request,'model_table.html',{'title':'Model Table','model_forms':model_forms})

def brand_table(request):
    if request.method=='POST':
        item=PhoneBrand.objects.get(pk=request.POST['id'])
        form = BrandForm(data=request.POST,instance=item)
        if form.is_valid():
            form.save()
        return redirect('http://127.0.0.1:8000/demo/brand/')
    else:
        brand_list=PhoneBrand.objects.all()
        brand_forms=[]
        for brand in brand_list:
            form = BrandForm(instance=brand)
            brand_forms.append((brand,form))
        return render(request,'brand_table.html',{'title':'Brand Table','brand_forms':brand_forms})

def category_table(request):
    if request.method=='POST':
        item=CategoryModel.objects.get(pk=request.POST['id'])
        form = CategoryForm(data=request.POST,instance=item)
        if form.is_valid():
            form.save()
        return redirect('http://127.0.0.1:8000/demo/category/')
    else:
        category_list=CategoryModel.objects.all()
        category_forms=[]
        for category in category_list:
            form = CategoryForm(instance=category)
            category_forms.append((category,form))
        return render(request,'category_table.html',{'title':'Category Table','category_forms':category_forms})
