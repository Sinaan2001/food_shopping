from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from .models import *
# Create your views here.
def home(request,c_slug=None):
    cat = categ.objects.all()
    c_page = None
    prodt = None
    products_list=None
    if c_slug!=None:
        c_page=get_object_or_404(categ,slug=c_slug)
        prodt= products.objects.filter(category=c_page,available=True)
    else:
        prodt= products.objects.all().filter(available=True)
    paginator=Paginator(prodt,3)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products_list = paginator.page(page)
    except(EmptyPage, InvalidPage):
        products_list = paginator.page(paginator.num_pages)
    return render(request,'index.html',{'pr':products_list , 'ct':cat})
def prodetails(request,c_slug,product_slug):
    try:
        prod=products.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'items.html',{'pr':prod})
def searching(request):
    prod=None
    query=None
    if 'form1' in request.GET:
        query=request.GET.get('form1')
        prod=products.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query))
    return render(request,'search.html',{'qr':query ,'pr':prod})