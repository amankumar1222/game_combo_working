from django.shortcuts import render , HttpResponse
import random
# Create your views here.

def rock_paper_scissior(user, comp):
    list_choices = { 1:'Rock', 2:'Paper', 3:'Scissior'}
    print(list_choices[comp])

    if user == comp:
        return "tie"
    elif user == 1 and comp == 3 or user == 3 and comp == 2 or user == 2 and comp == 3:
        return "You Win user"
    else:
         return "You loose Ai Win"


def rps(request):
    # user = int(input("Enter your choice :- 1:'Rock', 2:'Paper', 3:'Scissior' \n "))
    if request.method == "POST":
        user = request.POST.get('user')
        user = int(user)
    else:
        user = 3
    comp = random.randint(1,3)
    result = rock_paper_scissior(user,comp)
    return render(request, 'rps/rps.html' , {'result':result})


