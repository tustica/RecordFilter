from json.decoder import JSONDecodeError
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from main.models import Profile
import json
from django.core import serializers
import datetime
from datetime import tzinfo
import pytz
from json import dumps

def index(request):
    profiles = Profile.objects.all()
    data= serializers.serialize('json', profiles)
    return render(request, 'index.html', {'data': data} )

def addRecord(request):
    new_record = Profile.objects.create(first_name=request.POST['first_name'],
    last_name=request.POST['last_name'], email=request.POST['email'])
    return redirect('/')

def datadata(request):
    if request.method == 'POST':
        all = Profile.objects.all()
        list = []
        utc = pytz.UTC
        for each in all:
            from_date = request.POST['from_date'][10:25]
            to_date = request.POST['to_date'][10:25]
            # print(each.registered_at.replace(tzinfo=None))
            # print(datetime.datetime.strptime(from_date, "%Y-%m-%d"))
            database_time = each.registered_at.replace(tzinfo=None)
            if datetime.datetime.strptime(from_date, "%Y-%m-%d") <= database_time <= datetime.datetime.strptime(to_date, "%y-%m-%d"):
                date_dict = {
                    "id": each.id,
                    "first_name": each.first_name,
                    "last_name": each.last_name,
                    "registered_at": each.registered_at,
                    "email": each.email,
                }
                list.append(date_dict)
        return JsonResponse(list, safe=False)

    context = {
        'profiles': Profile.objects.all()
    }
    return render(request, 'index.html', context)

def ajaxCall(request):
    if request.method == "POST":
        all = Profile.objects.all()
        list = []
        for each in all:
            if request.POST.get('content')[5:20].lower() in each.first_name.lower():
                new_dict = {
                    "id": each.id,
                    "first_name": each.first_name,
                    "last_name": each.last_name,
                    "registered_at": each.registered_at,
                    "email": each.email
                }
                list.append(new_dict)
        return JsonResponse(list, safe=False)

        # else:
        #     none = "none";
        #     return JsonResponse({"none": none})

    context = {
        'profiles': Profile.objects.all()
    }
    return render(request, 'index.html', context)

