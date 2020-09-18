from django.http import HttpResponse
from django.shortcuts import render, redirect
from dockerInstance.tasks import create, get_all_containers, stop
from celery.result import ResultBase
import docker

# Create your views here.



def index(request):
    container_list = get_all_containers()

    context = {
        "containers":container_list
    }
    #return HttpResponse("hellow world")
    return render(request, 'dockerInstance/index.html', context)

def create_order(request):

    task = create.delay()
    response = redirect("/")
    return response

def stop_order(request):
    containerName = request.POST.get("containerObject",False)
    stop.delay(containerName)
    response = redirect("/")
    return response
