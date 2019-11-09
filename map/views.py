from django.shortcuts import render
from map.models import area,reasoning

# Create your views here.
def startjourney(request):
    return render(request,'map/before.html')

def rate(request):


    print("hi")
    if request.method == 'POST':
        print("hey")
        #print('hello')
        x=area(name="Hewlett Packard Avenue Road",rate=request.POST)
        print("hey1")
        if x.is_valid():
            x.save(commit = True)
            print("hey2")
    return render(request,'map/after.html')



def after(request):
    return render(request,'map/after.html')

def feedback(request):
    reasoning_list=reasoning.objects.all
    context={'reasoning_list':reasoning_list}

    return render(request,'map/feedback.html',context)

def thankyou(request):
    return render(request,'map/thankyou.html')
