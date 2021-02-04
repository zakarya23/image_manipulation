from django.shortcuts import render
import requests
import sys 
from subprocess import run, PIPE 

def button(request):
    return render(request,'home.html')

# def external(request): 
#     pic = request.FILES.get('photo')
#     # return('ss')
    
#     # out = run(sys.executable,['C://Users//zakry//Documents//Projects//myproject//test.py', pic], shell=False, stdout=PIPE)
#     # print(out)
#     return render(request, 'home.html')
#     #, {'data1': out}       ,{'data1':out.stdout}


def external(request):
    inp= request.POST.get('demo')
    print(inp)
    # out= run([sys.executable,'C://Users//zakry//Documents//Projects//myproject//hello.py',inp],shell=False,stdout=PIPE)
    # print(out)
    return render(request,'home.html')