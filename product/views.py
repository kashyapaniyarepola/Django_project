# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.files import File
import json
import os
from django.http import HttpResponseRedirect
from .forms import NameForm , SearchForm , ButtonForm



# Create your views here.

module_dir = os.path.dirname(__file__)  # get current directory
file_path = os.path.join(module_dir, 'product_list.txt')
try:
    f = open(file_path,'r')
except:
    print ("file not found")
post1 = []
for sentence in f:
    word_array = sentence.split(',')
    dictionary = {
        "id": word_array[0], "name": word_array[1], "price": word_array[-1][:-2]}
    post1.append(dictionary)
#y = json.dumps(post)
post=post1[-1:0:-1]
f.close()
 
def home(request):
    
    context={
        'posts' : post
    }
    if "search" in request.POST:
    # if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            context={
                'posts' : getsearch(name,post)
            }
            
    elif "id" in request.POST:
        form = ButtonForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            # name = form.cleaned_data['name']
            # price = form.cleaned_data['price']
            deleteProduct(id,post)
        #return HttpResponseRedirect('/')    
    return render(request, 'product/home.html' , context )


def add(request):

    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            addproduct(request,id,name,price)
            # f.write(id +","+name +"," +"$"+price + "\n")
            # post.append({"id":id , "name":name , "price": price})
            # home(request)
            # f.close()
            return HttpResponseRedirect('/')
        else:
            form = NameForm()
    return render(request, 'product/about.html' , {'title' :'Add Product'})

def addproduct(request,id,name,price):
    try:
        f = open(file_path,'a+')
    except:
        print ("error")
    f.write(id +","+name +"," +"$"+price + "\n")
    post.insert(0,{"id":id , "name":name , "price": price})
    f.close()
    context={
        'posts' : post
    }
    return render(request, 'product/home.html' , context )

def getsearch(name,post):
    p=[]
    name1 = name.capitalize()
    name2 = name.lower()
    for i in post:
        if (i["name"].__contains__(name1) or i["name"].__contains__(name2)):
            p.append(i)
    return (p)

def deleteProduct(id,post):
    for i in post:
        if (i["id"]==id):
            post.remove(i)
    try:
        f = open(file_path,'r')
    except:
        print ("error")
    a=f.readlines()
    for i in a:
        if i.__contains__(id):
            a.remove(i) 
    f.close()
    try:
        f = open(file_path,'w')
    except:
        print ("error")
    f.writelines(a)
    f.close()