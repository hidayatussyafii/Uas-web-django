from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import kategori, produk

# Creat your views here.

def members(requst):

    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def kategori(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())
                        
    context = {
        'contoh': 'ini variabel',
        'contoh': 'ini contoh lagi',
        'kategori':data,

    }
    return HttpResponse(template.render(context, request))
