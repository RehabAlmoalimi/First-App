from django.shortcuts import render
# Create your views here.

def index(request):
    x={'name':'Rehab'}
    return render(request,'pages/index.html',x)
def about(request):
    pass

