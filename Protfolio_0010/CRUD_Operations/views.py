from django.shortcuts import render
from django.http import HttpResponseRedirect
from CRUD_Operations.forms import insertForms,gallaryForm,newsForm
from .models import insertDatabase,image_gallary,newsTable

def insertFunc(request):
    if request.method=="POST":
        frm=insertForms(request.POST)
        if frm.is_valid():
            named=frm.cleaned_data['name']
            emaild=frm.cleaned_data['email']
            topicd=frm.cleaned_data['topic']
            described=frm.cleaned_data['describe']
            sqlset=insertDatabase(name=named,email=emaild,topic=topicd,describe=described)
            sqlset.save()
            return HttpResponseRedirect('/crud/insert/')
    else:
        frm=insertForms()
        
    # show bellow
    dataObject=insertDatabase.objects.all()     
    return render(request,'CRUD/insert.html',{"form":frm,"dataset":dataObject})

def showData(request):
    dataObject=insertDatabase.objects.all()
    return render(request,'CRUD/show.html',{"dataset":dataObject})

def updateDataValue(request,id):
    sqlset=insertDatabase.objects.get(id=id)
    if request.method=="POST":
        data=request.POST
        nameup=data.get('name')
        emailup=data.get('email')
        topicup=data.get('topic')
        describeup=data.get('describe')
        sqlset.name=nameup
        sqlset.email=emailup
        sqlset.topic=topicup
        sqlset.describe=describeup
        sqlset.save()
        return HttpResponseRedirect('/crud/show/')

    return render(request,'CRUD/update.html',{"dataset":sqlset})

def deleteData(request,id):
    data=insertDatabase.objects.get(id=id)
    data.delete()
    return HttpResponseRedirect('/crud/show/')

def gallaryLink(request):
    if request.method=="POST":
        frm=gallaryForm(request.POST,request.FILES)
        if frm.is_valid():
            frm.save()
    else:
        frm=gallaryForm()
    return render(request,'CRUD/form_to_gallary.html',{"form":frm})

def newsLink(request):
    if request.method == "POST":
        frm=newsForm(request.POST,request.FILES)
        if frm.is_valid():
            frm.save()
            frm=newsForm()
    else:
        frm=newsForm()
    show=newsTable.objects.all()
    return render(request,'CRUD/news.html',{"form":frm,"show":show})

def newsDelete(request,news_id):
    news=newsTable.objects.get(id=news_id)
    news.delete()
    return HttpResponseRedirect('/crud/news/')

def newsUpdate(request,news_id):
    news=newsTable.objects.get(id=news_id)
    if request.method == 'POST':
        data=request.POST
        files=request.FILES
        nameN=data.get('name')
        topicN=data.get('topic')
        desN=data.get('describe')
        filesN=files.get('field')
        news.name=nameN
        news.topic=topicN
        news.describe=desN
        news.field=filesN
        news.save()
        return HttpResponseRedirect('/crud/news/')
    return render(request,'CRUD/newsupdate.html',context={"news":news})