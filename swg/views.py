from django.shortcuts import render , HttpResponse
import random

# Create your views here.


# Snake Water gun or Rock Paper Scissors 
def gameWin(comp, you):
    # if two values are equal , declare a tie! 
    if comp == you:
        return None
    # check for all possiblities when computer choose s
    if comp == 's':
        if you == 'w':
            return False
        elif you =='gun':
            return True
    # check for all possiblities when computer choose w
    elif comp == 'w':
        if you == 'g':
            return False
        elif you =='s':
            return True
    
    # check for all possiblities when computer choose g
    elif comp == 'g':
        if you == 's':
            return False
        elif you =='w':
            return True
                

    



def swg(request):
        if request.method == "POST":
            user = request.POST.get('user')
        else:
            user = 3
            
        randNo = random.randint(1,3)
        if randNo == 1:
            comp ='s'

        elif randNo == 2:
            comp ='w'
        elif randNo == 3:
            comp ='g'
    
        # you = input("Your's Turn 1 Turn: Snake(s) Water(w) or Gun(g)?")
        a = gameWin(comp, user)
        print(f"Computer choose {comp}")
        print(f"You choose {user}")

        if a == None:
            result = "The game is a tie!"
        elif a:
            result ="You win!"
        else:
            result = "You Loose!"
        params = {'result':result}

        return render(request, 'swg/swg.html', params )