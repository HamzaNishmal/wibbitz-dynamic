import json

from django.shortcuts import render, redirect
from web.models import Subscribe, Customer,Feature

from django.http.response import HttpResponse
from django.urls import reverse


def index(request):

    customers = Customer.objects.all()
    features = Feature.objects.all()

    # print(customers)

    context = {
        "customers": customers,
        "features": features
    }

    return render(request,"index.html",context=context)


def subscribe(request):
    email = request.POST.get("email")

    if not Subscribe.objects.filter(email=email).exists():

        Subscribe.objects.create(
            email = email 
        )

        response_data = {
            "status" : "success",
            "title" : "Successfully subscribed demo version",
            "message" : "You subscribed to our demo version successfully"
    }
    else:
        response_data = {
            "status" : "error",
            "title" : "You are already subscribed",
            "message" : "You are already a member."
    }
    
    
    return HttpResponse(json.dumps(response_data),content_type="application/javascript")

    # if not Subscribe.objects.filter(email = email).exists():

    #     Subscribe.objects.create(
    #     email = email,
    #     )

    #     response_data = {
    #         "status" : "success",
    #         "title" : "You Successfully Registered",
    #         "message" : "You subscribe to our communitty successfully."
    #     }
    # else:
    #     response_data = {
    #         "status" : "error",
    #         "title" : "You are already Subscribed",
    #         "message" : "You are already a member."
    #     }

    # return HttpResponse(json.dumps(response_data), content_type = "application/javascript")