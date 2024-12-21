from django.shortcuts import render,redirect
import random

# Create your views here.


def display(request):
    return render(request,"display.html")





def result(request):
    user_choice = request.GET.get('choice')
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        outcome = "It's a draw!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        outcome = "You win!"
    else:
        outcome = "You lose!"

    context = {
        'user_choice': user_choice,
        'computer_choice': computer_choice,
        'outcome': outcome,
    }
    return render(request, 'result.html', context)

def again(request):
    return redirect('display')


