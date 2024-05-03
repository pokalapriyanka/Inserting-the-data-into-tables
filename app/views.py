from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *
from django.db.models.functions import Length

def insert_topic(request):
    tn=input('enter topicname')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    d={'QLTO':Topic.objects.all()}
    return render(request,'display_topics.html',d)

def insert_webpage(request):
    
    tn=input('enter topicname')
    #TO=Topic.objects.get(topic_name=tn)
    
    n=input('enter a name')
    u=input('enter url')
    e=input('enter email')
    
    '''We can use get method to get the parent table object but if parent table object 
    is not available it throws an error'''
    LTO=Topic.objects.filter(topic_name=tn)
    if LTO:
        TO=LTO[0]
        WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
        WO.save()
        d={'QLWO':Webpage.objects.all()}
        return render(request,'display_webpages.html',d)
    
def insert_access(request):
    

    i=int(input('enter id of webpage objects'))
    d=input('enter date')
    a=input('enter author')
    WO=Webpage.objects.get(id=i)
    AO=AccessRecord.objects.get_or_create(name=WO,date=d,author=a)[0]
    AO.save()
    d={'QLAO':AccessRecord.objects.all()}
    return render(request,'display_accessrecord.html',d)





def display_topics(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    return render(request,'display_topics.html',d)

def display_webpages(request):
    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.filter(topic_name='Cricket')
    QLWO=Webpage.objects.exclude(topic_name='Cricket')
    QLWO=Webpage.objects.all().order_by('topic_name')
    QLWO=Webpage.objects.filter(topic_name='Cricket').order_by('name')
    QLWO=Webpage.objects.all().order_by('-topic_name')
    QLWO=Webpage.objects.all().order_by(Length('name'))
    QLWO=Webpage.objects.all().order_by('name')[:10:]
    QLWO=Webpage.objects.all().order_by(Length('topic_name').desc())
    QLWO=Webpage.objects.all().order_by('name')[2:6:]
    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.filter(name__startswith='r')
    QLWO=Webpage.objects.filter(name__endswith='t')
    QLWO=Webpage.objects.filter(name__contains='a')
    QLWO=Webpage.objects.filter(name__in=['rohit'])
    QLWO=Webpage.objects.filter(name__in=['rohit','virat'])
    d={'QLWO':QLWO}
    return render(request,'display_webpages.html',d)

def display_accessrecord(request):
    QLAO=AccessRecord.objects.all()
    QLAO=AccessRecord.objects.filter(date__year='2024')
    QLAO=AccessRecord.objects.filter(date__month='5')
    QLAO=AccessRecord.objects.filter(date__day='11')
    QLAO=AccessRecord.objects.filter(date__year__gt='2023')
    QLAO=AccessRecord.objects.filter(date__year__gte='2023')
    QLAO=AccessRecord.objects.filter(date__year__lt='2024')
    QLAO=AccessRecord.objects.filter(date__year__lte='2024')
    QLAO=AccessRecord.objects.filter(date__month__gte='5')
    QLAO=AccessRecord.objects.filter(date__day__lt='12')
    QLAO=AccessRecord.objects.filter(date__day__gt='10')
    QLAO=AccessRecord.objects.filter(date__month__lt='10')
    QLAO=AccessRecord.objects.filter(date__month__lte='5')
    d={'QLAO':QLAO}
    return render(request,'display_accessrecord.html',d)