from django.shortcuts import render,redirect
from django import forms
from django.http import HttpResponseRedirect 
from django.urls import reverse
app_name="tasks"
class newTaskView(forms.Form):
    task=forms.CharField(label="Add new tasks",widget=forms.TextInput(attrs={
        'class':'w-full p-2 border border-grey-300 text-black rounded-md',
        'placeholder':'enter new task'
    }))
    

# Create your views here.
def index(request):
    if "tasks"  not in request.session:
        request.session["tasks"]=[]
    return render(request,"todolist/index.html",{"tasks":request.session["tasks"]})
def add(request):
    if request.method=="POST":
        form=newTaskView(request.POST)
        if form.is_valid():
            task=form.cleaned_data["task"]
            request.session["tasks"].append(task)
            request.session.modified=True
            return redirect("index")
        else:
            return render(request,"todolist/add.html",{'form':form})
    return render(request,"todolist/add.html",{
    'forms': newTaskView(),})
