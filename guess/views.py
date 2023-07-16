from django.shortcuts import render , HttpResponse
import random

import string
# Create your views here.


def guessing(user,num):
    print(num)
    if user != num:
        return "You loose"
    else:
        return "You win"
    
def guess(request):
    if request.method == "POST":
        user = request.POST.get('user')
        user = int(user)
    else:
        user = 3


    # user = int(input("Enter your number"))
    num = random.randint(1,5)
    result =  guessing(user,num)
    return render(request, 'guess/guess.html', {"result":result})