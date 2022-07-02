from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

list = ["talk", "study", "m***"]
available_tasks = [("play","play"), ("coding","coding"), ("web dev","web dev"), ("game dev","game dev")]

class NewTaskfform(forms.Form):
    task = forms.ChoiceField(choices=available_tasks)
    
# Create your views here.
def index(request):
    return render(request, "todo/index.html", {
        "list" : list,
        "form": NewTaskfform()
    })


def add(request):
    form = NewTaskfform(request.POST)
    val = form["task"]
    list.append(val.value)
    
    return HttpResponseRedirect(reverse('todo:index'))
    
    
    
